Python script to generate basic metal/semiconductor band diagrams.

The parameters are as follows:
* phi_m: metal workfunction 
* phi_s: semiconductor workfunction
* bandgap: semiconductor band-gap
* f: doping parameter (f = 0.5 to enfore E_F in the middle of the band-gap, above or below for n- and p-doped, respectively)
* when: either "before" or "after" contacting (aligning Fermi levels and band-bending)
* bending_k: effective bending sharpness

And several cosmetic parameters. 

Examples:

```
MetalSemiconductorDiagram(ax, phi_m=5.2, phi_s=4.5, bandgap=2.5, f=0.1, name_m='Au', name_s=f'MoS{sy.subscript_2}', when='before', fontsize=10)
```

<img width="612" height="676" alt="image" src="https://github.com/user-attachments/assets/2cfe8030-bb70-4eb9-8f25-840b8abac785" />

```
MetalSemiconductorDiagram(ax, phi_m=5.2, phi_s=4.5, bandgap=2.5, f=0.1, name_m='Au', name_s=f'MoS{sy.subscript_2}', when='after', fontsize=10)
```

<img width="612" height="676" alt="image" src="https://github.com/user-attachments/assets/7220d1b5-54f4-45ba-a759-a05358144f34" />

