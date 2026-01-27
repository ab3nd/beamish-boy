This is data collected from experiments with 1 bicore or two unconnected bicores on the same chip. The chip is a 74**HC**240, so it isn't using TTL switching levels (that would be the **HCT** family). H and C are for high-speed and CMOS. 

**50Msample_1MHz_single_bicore** - Single bicore present on the chip. Other pins were floating, which might not be great. 

**10Msample_1MHz_power_on** - 10 seconds including the circuit being turned on. 

**50Msample_1MHz_2_unlinked** and **50Msamples_1MHz_unconnected_bicores**- Two unlinked bicores, recording is during steady state (not immediately after turn on) 

**50Msample_1MHz_power_on_and_touch** - Power on and touching across the resistor on one of the bicores at about 9s, 17s, and 30s into the recording. Touching across the resistor reduces the resistance and so changes the frequency of the bicore. 

**5Msample_1MHz_power_on** and **5Msample_1MHz_power_on_2** - Same process: start recording and then power on. Records power-up behavior. 

I think that there's an effect where the bicores are coupled even if they're not really coupled. It looks like they fall into being 180 degrees out of phase even if there isn't a resistor between them. 

If I want a more serious exploration of this, I should design the things I want to record in advance. What I'd want is:

Single bicore, all other inputs grounded

	- Record startup twice (50Msample @ 1Mhz)

Dual bicores

- Record startup twice (50Msample @ 1Mhz)
- Record touch interference on second bicore

Alternatively, I could build a rig that automatically does something to alter the frequency of the second bicore at specific times, like using a relay to add a 5M resistor in parallel with the 1M resistor (total resistance ends up being 833.3k$\Omega$) on a timebase with a 555 timer or something. 
