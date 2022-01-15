def conv2D(inp, F, pad=0, stride=1):
    # Cross Correlation
    F = np.flipud(np.fliplr(F))

    # Gather Shapes of Kernel + Image + Padding
    n_H = inp.shape[0]
    n_W = inp.shape[1]
    f_H = F.shape[0]
    f_W = F.shape[1]


    # Shape of Output Convolution
    xOutput = int(((n_H - f_H + 2 * pad) / stride) + 1)
    yOutput = int(((n_W - f_W + 2 * pad) / stride) + 1)
    Z = np.zeros((xOutput, yOutput))

    # Apply Equal Padding to All Sides
    if pad != 0:
        inpPad = np.zeros((inp.shape[0] + pad * 2, inp.shape[1] + pad * 2))
        inpPad[int(pad):int(-1 * pad), int(pad):int(-1 * pad)] = inp
        print(inpPad)
    else:
        inpPad = inp

    # Iterate through inp
    for y in range(inp.shape[1]):
        # Exit Convolution
        if y > inp.shape[1] - f_W:
            break
        # Only Convolve if y has gone down by the specified Strides
        if y % stride == 0:
            for x in range(inp.shape[0]):
                # Go to next row once F is out of bounds
                if x > inp.shape[0] - f_H:
                    break
                try:
                    # Only Convolve if x has moved by the specified Strides
                    if x % stride == 0:
                        Z[x, y] = (F * inpPad[x: x + f_H, y: y + f_W]).sum()
                except:
                    break


    return Z