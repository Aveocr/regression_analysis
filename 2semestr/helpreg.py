import numpy as np



def pmatrix(a, digit : int =3, T : bool =False):
    """Returns a LaTeX bmatrix
    :a: numpy array
    :returns: LaTeX bmatrix as a string
    """
    if len(a.shape) > 2:
        raise ValueError('bmatrix can at most display two dimensions')
    lines = str(np.round(a, digit)).replace('[', '').replace(']', '').splitlines()
    rv = [r'\begin{pmatrix}']
    if not T:
        rv += ['  ' + ' & '.join(l.split()) + r'\\' for l in lines]
    else:
        rv += ['  ' + '\\\\ '.join(l.split()) for l in lines]
    rv +=  [r'\end{pmatrix}']
    return '\n'.join(rv)



def s_oct(y, y_pred, n):
    return np.round(np.sum((y-y_pred)**2) / (len(y) - n), 3)
    
