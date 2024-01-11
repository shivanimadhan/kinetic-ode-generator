import numpy as np

c0 = [0.005, 0.0, 1.5, 1.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

def kinetic_odes(t, c):
	kd = 100000.0
	kpAAA = 30.6
	kpAAB = 87.6
	kpABA = 0.735
	kpABB = 1.52
	kpBAA = 12.2
	kpBAB = 36.8
	kpBBA = 0.311
	kpBBB = 0.643
	kdpBB = 0.0
	ktcAA = 0.0
	ktcAB = 0.0
	ktcBB = 0.0
	ktdAA = 0.0
	ktdAB = 0.0
	ktdBB = 0.0

	dcdt = np.zeros_like(c)

	dcdt[0] = -kd*c[0]
	dcdt[1] = kd*c[0] + -kpAAA*c[1]*c[2] + -kpBBB*c[1]*c[3]
	dcdt[2] = -kpAAA*c[1]*c[2] + -kpAAA*c[2]*c[4] + -kpBBA*c[2]*c[5] + -kpAAA*c[2]*c[6] + -kpABA*c[2]*c[7] + -kpBAA*c[2]*c[8] + -kpBBA*c[2]*c[9]
	dcdt[3] = -kpBBB*c[1]*c[3] + -kpAAB*c[3]*c[4] + -kpBBB*c[3]*c[5] + -kpAAB*c[3]*c[6] + -kpABB*c[3]*c[7] + -kpBAB*c[3]*c[8] + -kpBBB*c[3]*c[9] + kdpBB*c[9] + kdpBB*c[9]
	dcdt[4] = kpAAA*c[1]*c[2] + -kpAAA*c[2]*c[4] + -kpAAB*c[3]*c[4]
	dcdt[5] = kpBBB*c[1]*c[3] + -kpBBA*c[2]*c[5] + -kpBBB*c[3]*c[5]
	dcdt[6] = kpAAA*c[2]*c[4] + -kpAAA*c[2]*c[6] + kpAAA*c[2]*c[6] + -kpAAB*c[3]*c[6] + kpBAA*c[2]*c[8] + -ktcAA*c[6]*c[6] + -ktcAA*c[6]*c[8] + -ktcAB*c[6]*c[7] + -ktcAB*c[6]*c[9] + -ktdAA*c[6]*c[6] + -ktdAA*c[6]*c[8] + -ktdAB*c[6]*c[7] + -ktdAB*c[6]*c[9]
	dcdt[7] = kpAAB*c[3]*c[4] + kpAAB*c[3]*c[6] + -kpABA*c[2]*c[7] + -kpABB*c[3]*c[7] + kpBAB*c[3]*c[8] + kdpBB*c[9] + -ktcAB*c[6]*c[7] + -ktcAB*c[8]*c[7] + -ktcBB*c[7]*c[7] + -ktcBB*c[7]*c[9] + -ktdAB*c[6]*c[7] + -ktdAB*c[8]*c[7] + -ktdBB*c[7]*c[7] + -ktdBB*c[7]*c[9]
	dcdt[8] = kpBBA*c[2]*c[5] + kpABA*c[2]*c[7] + -kpBAA*c[2]*c[8] + -kpBAB*c[3]*c[8] + kpBBA*c[2]*c[9] + -ktcAA*c[6]*c[8] + -ktcAA*c[8]*c[8] + -ktcAB*c[8]*c[7] + -ktcAB*c[8]*c[9] + -ktdAA*c[6]*c[8] + -ktdAA*c[8]*c[8] + -ktdAB*c[8]*c[7] + -ktdAB*c[8]*c[9]
	dcdt[9] = kpBBB*c[3]*c[5] + kpABB*c[3]*c[7] + -kpBBA*c[2]*c[9] + -kpBBB*c[3]*c[9] + kpBBB*c[3]*c[9] + -kdpBB*c[9] + -kdpBB*c[9] + kdpBB*c[9] + -ktcAB*c[6]*c[9] + -ktcAB*c[8]*c[9] + -ktcBB*c[7]*c[9] + -ktcBB*c[9]*c[9] + -ktdAB*c[6]*c[9] + -ktdAB*c[8]*c[9] + -ktdBB*c[7]*c[9] + -ktdBB*c[9]*c[9]
	dcdt[10] = ktcAA*c[6]*c[6] + ktcAA*c[6]*c[8] + ktcAA*c[8]*c[8] + ktcAB*c[6]*c[7] + ktcAB*c[6]*c[9] + ktcAB*c[8]*c[7] + ktcAB*c[8]*c[9] + ktcBB*c[7]*c[7] + ktcBB*c[7]*c[9] + ktcBB*c[9]*c[9] + ktdAA*c[6]*c[6] + ktdAA*c[6]*c[8] + ktdAA*c[8]*c[8] + ktdAB*c[6]*c[7] + ktdAB*c[6]*c[9] + ktdAB*c[8]*c[7] + ktdAB*c[8]*c[9] + ktdBB*c[7]*c[7] + ktdBB*c[7]*c[9] + ktdBB*c[9]*c[9]

	return dcdt