"""
Visualisation utilities for the Model.

You don't need to read or understand this code!

Author: Matthew Alger

Updated 20 May 2020 by Malcolm.
"""

import base64
import lzma

import matplotlib.pyplot as plt
import numpy

def plot_volumes(volumes):
    """Plot a list of volumes, in litres, against actual Lake George volumes.

    Parameters
    ----------
    volumes : [float]
        List of volumes, in litres, like output by lake_george_simple_model.
    """
    lgd = b'/Td6WFoAAATm1rRGAgAhARYAAAB0L+Wj4A/RB5xdABiOXARmN07zFZFMzRkdPJlEM5717W' +\
          b'kTa6QJZTiTMmDCvEoaeY2/hZSQTqmAG72VrutkbTk0X81VxizGkX7hAnsEPbqRMYLqs1K7' +\
          b'73SPla3TGeF/i18v4z7sIsnGIAs0nOCfiYKJMwYV79ny8fsk/CDRL7qpWyAOu//64AXXfR' +\
          b'TAvYfLixyDfNuxD43hNOnNrivVrDvv94TLCbS4IDLtL+v36Y7Xie3FwPtwO0WRSrnaBY/4' +\
          b'sWlQc4PTsvD/64SnBBaTvxrSrDJwZV3qMcin1SCoibMGrkO0f7zhGEC15q/2ZEHNjCUx7A' +\
          b'RLdGayhOdItEg8LiJmzg7/uyPaFRANyy/woMF+Yzf/SJTA2Fz+K9k8OL2gKg/1ty6QisJ4' +\
          b'tc8OkcvZvTpLvjGqQVy7fSaRLDTPJGZNn05cL95825Ic7JtXB0OIT0HICfnFUObfVctAeP' +\
          b'aiFDsdcMsagJBEW8e/IbCGt5BH2GeLoodOEcL0XwZnfZX7JNvZAJBYR5kN+OcCZgua1Qh5' +\
          b'V3we2SBL9jZL1WYSgoYSoyGPCA79VzOko+pM5WJArSWf8oDWBMCnWUjpugmF7N/29m/QK7' +\
          b'KeEshwprc3UsgxiFBNGP6qW8rWDJZf9yVo1Yu0lbcTzCIDNe7Aq3JrR3EcY+p36FtH3rOx' +\
          b'H/ljGO+GDGXO1LaL/GBBWaqHcC7Di5WsgnhUK6aBj1tY4VLc8TsrB4OguCO4h385MTIGPA' +\
          b'RgW0QUbIb64eNF7A+5D0SeAGWxpcVxLfUOvMwQeXWYw7B6WmHOD0Z8Sg/PrCrI/FCGld32' +\
          b'U130fDvAlSiJUZvIZR0c2GJeGHFvlWzM58H19UPaQl30F4Zt2LLMyG2AxNEwwdRkrGG92Y' +\
          b'HshOyoPJkPWGvRPs7QMQqRmAI+2ywoCq/AP4iKsiSkndmgGWkX0c1Gp+rOX/lAtQLWJeaU' +\
          b'xMqq2tByh+KqydKdZrrIjwF83Z0bkKtmK2+ZKYxvi6FgkCHpYAZaq3WMG8WqVbo/GBRDzg' +\
          b'DjHXnkmJImNMXqNYN1lt5lwuCrPkhcs2wMlPy/TLb6qS5B4QfYGZkQEAGfW0YAICWdNF7b' +\
          b'tmCmd/QTQbme1Chkqtcg+QCPjlALoezSwtI5f9koN8AZ9AACiRYcniaiM0FqhtqBsxNqTj' +\
          b'3XaH9cL2k6FqrV2pvojKes0JzNN/eg1Acvlm6G3F5RDo7EXZlUXCiQr1V8TaA6gvvrW76H' +\
          b'0WEaEYwh1SjyKlTEqifb3CG7umLDQ3q2uYghdu5qleP8zPX5ynNKvwYwpePjIM1tR2h7eP' +\
          b'VQSor0CcLHEBDwJWev4mxwsRfmQO2LVKr6oIaHeQSe+iLRPcB3SD/FV/yRsCHZdVDLrAbC' +\
          b'NimBgcxZCfP2rb7lq41ZhRqgfuQ5rnMdNPR6fgy8pJbjb/XsVq3opY9mOKEfBj5SJqdHbL' +\
          b'HWhApXbgCxIMzHaQxg/NRLsxMxBhlmWTPyuhA+c0g7RXtvfdhv+0ZdcJHDd7PIN53uoCqO' +\
          b'54GMIa+TuR3YzPEGzCaWwyRUdW/m2QQHe+smx0SJ5qBTvMTeZbt/RT1C+pUfM7YQceNDAz' +\
          b'6ccFh/jHe8hNYDPKIEVoby1/KnA6FgoRc8ZwIdREZClW9aWR9u5hOfcOq733k1wc2sN61P' +\
          b'v4KJoUhIY/Kn0JZACvexy8yDMoBsrcTTJFMgk8jSXkYNMijKpqYU/lbsqQ0jl5EspruVev' +\
          b'qZmtTQJzlbpeYykbx1X7f36to1YejRMhNBbmljOfEM7UEjBrAHoPrC514nwbw++C9cocO1' +\
          b'KZ2E4wIpFrdTxcVF3a7rRBvSro+I96I+5FwSaBzaYtYjCLpNfVVhYX54pW30Wjy3MXTxKj' +\
          b'OUveFfZc5aB7PF2a1D4zyGJMhz9GepYhWb83pZ8uLXlari8oDZwhGh+OQyXeYUwIUnp9n3' +\
          b'IAhJkrMS29P6cVcp2jqYVxdW0kaJ5PbgNsljlu4jSIanvjTxBwjd3suTGc0UPdP8OL48Dx' +\
          b'i61GTrhquDuBBF3gAszoo33cnojR8Rsq9GnFZXscewUwgHGHAFGQA6GZ6eOKRo0NuU3DFa' +\
          b'U4s5DaUAt86afAM0/tq7uIF/f4igwt1gXmLTGY26gx+dW4yWYKqZzmxzzmKvQvTrJHt5xv' +\
          b'JWEtoh7HfM+cvCLF/Af6CxvxtZ2igmcJY1qE5Bahy/WNK7YgvtWCl0Igsqb2qu2iXrKZt6' +\
          b'HGn+yO4f7bdwFs9vU65LERrI6kPO+kA09FKENZJV/bL1jr8bXQ3e/jmtdJwH8BYIWwHW2K' +\
          b'MwyEgBnlpG8D70VopJ4exKuX5PSxwy1wWOJ6SeH/TLEZRxa9lS14Y6tQq5X1qRKJyiErvj' +\
          b'ccLs8iNH33KtQO6825BNtOyXc59DFzJOXzoR5dME0/vfqCb74l3GiRh1i6G3WE0xM0WgC7' +\
          b'S6KWb0DpA3sespnMqMtO0Q/uHoiaHguxHVJPhEYw7qJPVoeGxp+ztAPfWJ7yzFpqoSLRxP' +\
          b'CbVDf925OQtQo0mbfWVtgj8C/VzaZxgRfgFR8sDuUyCRAsHjOHFiYPWMsykfMmb84QpMe2' +\
          b'1nDHZINecq53E+Y/rJSBPWjmqOv+egnshDBsNGIJewCNjspyEApAiyujI7V4AAAbgP0h8A' +\
          b'AEtHuyyxxGf7AgAAAAAEWVo='
    lgv = list(map(int, lzma.decompress(base64.b64decode(lgd)).split(b'|')))
    plt.plot(range(len(volumes)), volumes, label='Given volume')
    plt.plot(range(348), lgv, label='Actual Lake George volume')
    plt.xlabel('Month')
    plt.ylabel('Volume ($L$)')
    plt.legend(loc='best')
    plt.show()


def volume_to_area(volume):
    """ Convert the volume of Lake George (in litres) to area (in square metres).
    Parameters
    ----------
    volume : float
        Volume in litres.

    Updated 20/5/2020, MAM: prevent negative area when volume < 1e8.
    """
    pf1 = [4.60493943e-25, -7.14202851e-14, 4.34050787e-03, -2.51895310e+06]
    pf2 = [7.68888893e-27, -4.92231144e-15, 1.15000089e-03, 4.83203509e+07]
    if volume < 6e10:
        return max(0,numpy.polyval(pf1, volume)) # 20/5/2020, MAM.
    return numpy.polyval(pf2, volume)
