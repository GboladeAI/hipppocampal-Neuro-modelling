import numpy as np
from scipy.special import comb
from scipy import stats, integrate
from scipy.sparse import csr_matrix
import math
import pandas as pd
from itertools import combinations
import random
#import numba
from sklearn.model_selection import train_test_split
import pylab
from pandas.util.testing import assert_frame_equal


def fitPopTrack(data):
    alpha = 0.02
    length = len(data.columns)
    columns = data.columns

    p_xi_givenk = pd.DataFrame(index=range(length + 1), columns=data.columns)  # % Initialize
    pattern_select = []
    data['count'] = data.sum(axis=1)
    count_values = data['count'].values
    n = length

    count = pd.DataFrame(count_values, columns=['count'])  # count number of units at each bin
    count['freq'] = count.groupby('count')['count'].transform('count')
    pk = pd.DataFrame(0, index=range(26), columns=['freq'])
    count = count.drop_duplicates('count').set_index('count')
    pk.update(count)

    pk2 = pk + alpha  # Add regularising pseudocount from dirichlet prior
    pk2['p_k'] = pk2['freq'] / pk2['freq'].sum(axis=0)  # Normalise to get probability distribution
    p_k = pk2['p_k'].values
    nr = range(length + 1)

    for i in nr:

        if i == 0:
            p_xi_givenk.iloc[i] = 0  # Silent state, all OFF

        if i == length:
            p_xi_givenk.iloc[i] = 1  # All ON

        if i > 0 and i < length:

            pattern_select = data[data['count'] == i]
            npop = len(pattern_select)  # Number of such timesteps
            mu = i / n  # Mean of prior

            for j in columns:  # loop over popuation levels

                nactive_vec = sum(pattern_select[j])  # number of times each neuron active
                p_xi_givenk.iloc[i][j] = (3 * mu + nactive_vec) / (npop + 3)

    data = data.drop('count', axis=1, inplace=True)

    return p_xi_givenk, p_k


def Compute_ak(p_xi_givenk, brute_thresh, nsamples):
    length = len(p_xi_givenk) - 1
    ak = []  # Initialize
    nr = range(length + 1)
    the_list = range(length)

    for k in nr:

        if k == 0:
            ak.append(1)  # Silent state

        if k == length:
            ak.append(1)  # All ON state

        if k < length and k > 0:

            pvec = p_xi_givenk[p_xi_givenk.index == k]  # Select p_xi_givenk vector for correct k
            nwords_wkactive = comb(length, k, exact=True)  # Number of words with k active
            pvec_np = pvec.values[0]

            if nwords_wkactive < brute_thresh:

                patternmat = list(combinations(the_list, k))
                cumsumpword = 0;

                for i in range(nwords_wkactive):
                    onindsk = list(patternmat[i])  # ON neurons
                    offindsk = list(set(the_list) - set(onindsk))  # OFF neurons
                    cumsumpword = cumsumpword + np.prod(pvec_np[[onindsk]]) * np.prod(1 - pvec_np[[offindsk]])

                ak.append(cumsumpword)

            else:

                if pvec.std(axis=1).values[0] == 0:  # If homogeneous (due to lack of data at given k)

                    ak.append(nwords_wkactive * (pvec_np[1] ** k) * (1 - pvec_np[1]) ** (length - k))

                else:  # If heterogeneous

                    cumsumpword = 0;
                    ns = range(nsamples)

                    for i in ns:
                        onindsk = list(random.sample(the_list, k))  # Choose k random ON neurons
                        offindsk = list(set(the_list) - set(onindsk))  # OFF neurons
                        cumsumpword = cumsumpword + np.prod(pvec_np[[onindsk]]) * np.prod(1 - pvec_np[[offindsk]])

                    ak.append(cumsumpword * (nwords_wkactive / nsamples))

    return ak


def Compute_px(data, ak, p_k, p_xi_givenk):
    length = len(p_xi_givenk) - 1
    px = []
    p_xi_givenk_np = p_xi_givenk.values
    data_index_np = range(len(data.index.values))
    data_sparse = csr_matrix(data.values)
    nr = range(length)

    for i in data_index_np:
        oninds = data_sparse[i].nonzero()[1]  # ON neurons
        offinds = list(set(nr) - set(oninds))  # OFF neurons
        kactive = len(oninds)  # Number of ON neurons
        arr_com = np.concatenate((p_xi_givenk_np[kactive][[oninds]], (1 - p_xi_givenk_np[kactive][[offinds]])))
        # Pattern probability
        px.append(p_k[kactive] * np.prod(arr_com) / ak[kactive])

    return px