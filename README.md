# Secure Texting over Multiple Untrusted Non-cooperative Networks (stn)
Radio systems are vulnerable to cyber attacks. This may be in the form of denial of service, jamming, interference and blocking among others. This may be a huge problem especially in high priority domains such as healthcare emergencies and military missions. In the case of military battlefield, the adversary relies on the identity of the user (combat soldier) to intercept or block the message. Communicating over open civilain cellular networks is one solution that can be applied to avoid intentional malcious attacks to aid soldiers in the ground. Such a system referred here as `windtexter` relies on anonymity and camouflage as shown in `Figure 1`. 

## Figure 1 Illustration of Secure Texting over Open Non-Cooperative Networks.
<p align="center">
  <img src="/docs/windtexter.png" />
</p>

This repository provides a code to simulate an attack scenario for users communicating over cellular networks (2G, 3G, 4G and 5G). The model simulates a jammer moving over space and time and broadcasting a replica signal to prevent the user from communicating with the cellular transmiter. This is simulated across all the four cellular generation technologies.

Citation
---------
Osoro, B., & Oughton, E. (2022). Spatial Modelling of Jamming Secure Texts over Non-cooperative Networks (December 18, 2022).

Example Method
==============

The spatial modelling approach is implemented. The transmitter, user and the jammers are treated as agents in a 15 X 15 km grid. The transmitter and interceptors aree is static while the users move randomly within the grid. The difference in euclidean distance between the transmitter and the jammer results in various interference power.

Similarly, the user and transmitter distance changes resulting to various receiver power. The Euclidean distance in both cases (user  and jammer) results in various path loss. The path loss contributes to differing interfernce and received power causing varying signal to interference plus noise (SINR). `Figure 2` illustrates this method.

## Figure 2 Spatial Modelling of the SINR.
<p align="center">
  <img src="/docs/Box_model.png" />
</p>

In the second model, a covert secure texting strategy is implemented. In this case, a single message is hidden in plain text, separated into different parts and transmitted through multiple untrusted non-cooperative networks to avoid detection. `Figure 3` illustrates the method.

## Figure 3 Covert secure texting simulation.
<p align="center">
  <img src="/docs/method_covert .png" />
</p>

Example Results
==============

The sample jamming, secure texting and socio-economic results are shown in `Figure 4`, `Figure 5` and `Figure 6`.

## Figure 4 Radio signal results from the spatial modeling in a 15 km ×15 km grid with 5 transmitters and interceptors for different cellular generations 
<p align="center">
  <img src="/docs/loss_profile.png" />
</p>

## Figure 5 Simulated probabilistic results of secure texting in a jamming environment. 
<p align="center">
  <img src="/docs/density_plots.png" />
</p>

## Figure 6 Simulated cost results due to interception and blocking of mission critical messages by different implementation strategy of anti-jamming techniques.
<p align="center">
  <img src="/docs/socio_costs.png" />
</p>

Required Data
==============