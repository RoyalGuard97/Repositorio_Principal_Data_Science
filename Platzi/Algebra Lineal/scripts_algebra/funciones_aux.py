def graficarVectores(vecs,cols,alpha = 1):
    import matplotlib.pyplot as plt
    import numpy as np
    plt.figure()
    plt.axvline(x=0,color="grey",zorder=0)
    plt.axhline(y=0,color="grey",zorder=0)

    for i in range (len(vecs)):
        x = np.concatenate([[0,0],vecs[i]])
        plt.quiver([x[0]],[x[1]],[x[2]],[x[3]],angles="xy",scale_units="xy",scale=1,color = cols[i],alpha=alpha)