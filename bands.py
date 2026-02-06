import numpy as np
import matplotlib.pyplot as plt
import symbols as sy

def MetalSemiconductorDiagram(ax, phi_m, phi_s, bandgap, f, name_m='Au', name_s=f'MoS2', when='after', color_m=[1,0.9,0,0.5], bending_k=2, fontsize=8):
	'''
	Generates the diagram
	'''

	x_m = np.linspace(-1, 0, 100)
	x_s = np.linspace(0, 2, 100)

	# vacuum levels
	vacuum_m = 0*x_m
	vacuum_s = 0*x_s

	# fermi levels (before contact)
	EF_m = 0*x_m - phi_m
	EF_s = 0*x_s - phi_s
	EF_s_after = EF_m
	EF = np.mean(EF_m)

	# bandgap (before contact)
	Ec_s = EF_s+(1-f)*bandgap
	Ev_s = EF_s-(f)*bandgap

	# effect of contacting
	Delta = EF_s-EF_m
	Ec_s_after = Ec_s - Delta*(1-np.exp(-bending_k*x_s))
	Ev_s_after = Ev_s - Delta*(1-np.exp(-bending_k*x_s))

	# plotting the metal 
	ax.axvline(0, ls=':', color=[0,0,0,0.5], lw=1)
	ax.plot(x_m, vacuum_m, '--', color=[0,0,0,0.5], lw=1)	
	ax.plot(x_m, EF_m, '--k')

	# block
	ax.fill_between(x_m, x_m*0-10, x_m*0-phi_m, color=color_m, edgecolor=[0,0,0,0])

	# text
	ax.text(0.10, 0.80, s=f'{name_m}\n'+rf'$\phi$ = {phi_m:.1f} eV', transform=ax.transAxes, fontsize=fontsize, color='black', ha='left')
	ax.text(0.90, 0.80, s=f'{name_s}\n'+rf'$\phi$ = {phi_s:.1f} eV', transform=ax.transAxes, fontsize=fontsize, color='white', ha='right')
	ax.text(0.90, 0.05, s=f'Eg = {bandgap:.2f} eV', transform=ax.transAxes, fontsize=fontsize, color=[1,1,1], ha='right')

	if when == 'before':
		# plot (before contact)
		ax.plot(x_s+1, vacuum_s, '--', color=[0,0,0,0.5], lw=1)
		ax.plot(x_s+1, EF_s, '--k')
		ax.plot(x_s+1, Ec_s, '-b')
		ax.plot(x_s+1, Ev_s, '-r')

		ax.axvline(1, ls=':', color=[0,0,0,0.5], lw=1)
		ax.fill_between(x_s+1, x_s*0-10, Ev_s, facecolor=[1,0,0,0.5], edgecolor=[0,0,0,0])
		ax.fill_between(x_s+1, Ec_s, x_s*0, facecolor=[0,0,1,0.5], edgecolor=[0,0,0,0])
		
	if when == 'after':
	# plot (after contact)
		ax.plot(x_s, vacuum_s, '--', color=[0,0,0,0.5], lw=1)
		ax.plot(x_s, EF_s_after, '--k')
		ax.plot(x_s, Ec_s_after, '-b')
		ax.plot(x_s, Ev_s_after, '-r')
	
		ax.fill_between(x_s, x_s*0-10, Ev_s_after, facecolor=[1,0,0,0.5], edgecolor=[0,0,0,0])
		ax.fill_between(x_s, Ec_s_after, x_s*0, facecolor=[0,0,1,0.5], edgecolor=[0,0,0,0])

	ax.axis('off')
	ax.set_ylim([EF-3, 0.1])



# Example 1: MoS2/Au contact before contacting

phi = 4.5
eg = 2.5
f = 0.1

fig, ax = plt.subplots(num='Band Diagram of MoS2/Au before contacting', tight_layout=True, figsize=(5,5))
MetalSemiconductorDiagram(ax, phi_m=5.2, phi_s=phi, bandgap=eg, f=f, name_m='Au', name_s=f'MoS2', when='before', fontsize=10)

fig, ax = plt.subplots(num='Band Diagram of MoS2/Au after contacting', tight_layout=True, figsize=(5,5))
MetalSemiconductorDiagram(ax, phi_m=5.2, phi_s=phi, bandgap=eg, f=f, name_m='Au', name_s=f'MoS2', when='after', fontsize=10)

plt.show()


# Example 2: MoS2/Au contacts with varying work functions, bandgaps and doping levels

phi_array = np.linspace(4.5, 5.5, 4)
Egs_mos2 = np.linspace(2.5, 1.2, 3)
doped_f = [0.2, 0.5, 0.8]

for f in doped_f:

	if f==0.2:
		name = f'P-doped  '
	elif f==0.5:
		name = f'Intrinsic'
	elif f==0.8:
		name = f'N-doped  '

	fig, axs = plt.subplots(ncols=len(Egs_mos2), nrows=len(phi_array), tight_layout=True, sharex=True, sharey=True, num=f'Band Diagram Au/MoS2 ({name.replace(' ', '')})', figsize=(5,6))

	for i, phi_s in enumerate(phi_array):
		for j, eg in enumerate(Egs_mos2):
			ax = axs[i,j]
			MetalSemiconductorDiagram(ax, phi_m=5.2, phi_s=phi_s, bandgap=eg, f=f, fontsize=6)

plt.show()
