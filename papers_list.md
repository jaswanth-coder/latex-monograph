# Monograph Content Mapping: Journals, Archive Papers, and Conference Papers

This document provides a comprehensive mapping of research papers authored by Prof. T. G. Venkatesh and his research group to the 15 chapters of the research monograph:
**"Design and Performance Evaluation of the Medium Access Layer Protocol of Wireless Networks: A Comprehensive Synthesis of WLAN, 5G, IoT, and Analytical Modeling"**.

Publications are organized per chapter under three clear subheadings:
- **Journals** (from the repository `papers/` and `WIFI 7 and 8/`)
- **Papers in Archive** (arXiv / TechRxiv preprints)
- **Conference Papers** (IEEE / ACM / IET proceedings)

Every entry includes:
1. **Paper Title**
2. **Authors**
3. **Mapped Topic in Monograph**
4. **Venue / File Reference**

---

# Part I: Foundations and Standards

## Chapter 1: Mathematical Preliminaries
*Focus: Discrete-Time Markov Chains (DTMC), Renewal Reward Theory, Markov Decision Processes (MDP), Queueing Theory ($M/M/1$, $M/G/1$ Pollaczek-Khinchin), Fixed-Point Analysis, Fluid Limit Approach, and Stochastic Geometry (Poisson Point Processes, Campbell's Theorem, Laplace transforms).*

### Journals
- **Fluid-Limit Model for Dynamic MU-OFDMA Resource Allocation of Wi-Fi 6 Networks**
  - *Authors:* Aparna Behara and T. G. Venkatesh
  - *Mapped Topic:* Fluid Limit Approach, Mean Field Approximation, Ordinary Differential Equation (ODE) modeling of dynamic subcarrier/RU allocation in multi-user networks.
  - *Venue / File:* IEEE Networking Letters (2021) / `papers/Fluid-Limit_Model_for_Dynamic_MU-OFDMA_Resource_Allocation_of_Wi-Fi6_Networks.pdf`

---

## Chapter 2: Wireless Local Area Networks
*Focus: CSMA/CD vs. CSMA/CA, RTS/CTS, Bianchi 2-D DTMC model, unsaturated traffic modeling, delay jitter, QoS & IEEE 802.11e EDCA, IEEE 802.11ad directional MAC (PGQS queuing), Multi-Packet Reception (MPR) MAC (Pure ALOHA order statistics, NP/1P-CSMA renewal models, Adaptive Backoff DCF, Adaptive EDCA), IEEE 802.11ax MU-OFDMA / MU-MIMO / Hybrid Access, SIC MAC, and Full-Duplex (SM-FD & C-FD MAC with channel sounding).*

### Journals
- **Design and analysis of IEEE 802.11 based Full Duplex WLAN MAC protocol**
  - *Authors:* Ankit Kumar Gupta and T. G. Venkatesh
  - *Mapped Topic:* Synchronized Mode Full-Duplex (SM-FD) MAC, Address-4 piggybacking, preamble alignment, 3 coupled Markov chains for SA nodes, active contenders, and transceiver operating status.
  - *Venue / File:* Computer Networks, Elsevier, Vol. 210, 108933 (2022) / `papers/Design and analysis of IEEE 802.11 based Full Duplex WLAN MAC protocol.pdf`
- **Design and performance analysis of a MAC protocol for wireless LANs supporting multipacket reception**
  - *Authors:* Arun I. B and T. G. Venkatesh
  - *Mapped Topic:* Adaptive Backoff MPR-DCF algorithm, state-dependent step decrement $d(i) = K - i$, restoration of renewal properties in multi-packet reception channels.
  - *Venue / File:* IEEE Transactions on Wireless Communications (2014) / `papers/Design and performance analysis of a MAC protocol for wireless LANs supporting multipacket reception.pdf`
- **Analysis of carrier sense multiple access protocols for channels supporting multipacket reception**
  - *Authors:* Arun I. B and T. G. Venkatesh
  - *Mapped Topic:* Renewal-reward theory for Non-Persistent CSMA (NP-CSMA) and 3-state DTMC transition matrix for 1-Persistent CSMA (1P-CSMA) under MPR capabilities.
  - *Venue / File:* IET Communications, Vol. 9, Iss. 8, pp. 1097–1105 (2015) / `papers/IET Communications - 2015 - Indira Balan - Analysis of carrier sense multiple access protocols for channels supporting.pdf`
- **Performance analysis of contention-based access periods and service periods of 802.11ad**
  - *Authors:* C. Hemanth and T. G. Venkatesh
  - *Mapped Topic:* Millimeter-wave 60 GHz directional MAC, Contention-Based Access Period (CBAP) beamforming contention, and Service Period (SP) scheduled intervals.
  - *Venue / File:* IET Networks, Vol. 3, Iss. 4, pp. 270–278 (2014) / `papers/IET Networks - 2014 - Hemanth - Performance analysis of contention‐based access periods and service periods of 802 11ad.pdf`
- **Performance Analysis of Service Periods (SP) of the IEEE 802.11ad Hybrid MAC Protocol**
  - *Authors:* C. Hemanth and T. G. Venkatesh
  - *Mapped Topic:* Pseudo-Gated Quasi-Static (PGQS) queueing model, non-zero overhead interval transitions, boundary condition derivations, and delay jitter bounds.
  - *Venue / File:* IEEE Transactions on Mobile Computing, Vol. 15, No. 5, pp. 1224–1237 (2016) / `papers/Performance_Analysis_of_Service_Periods_SP_of_the_IEEE_802.11ad_Hybrid_MAC_Protocol.pdf`
- **Performance analysis of the service periods of IEEE 802.11ad hybrid MAC protocol with variable packet lengths**
  - *Authors:* C. Hemanth and T. G. Venkatesh
  - *Mapped Topic:* IEEE 802.11ad directional service periods with general/variable packet length distributions.
  - *Venue / File:* Transactions on Emerging Telecommunications Technologies (2019) / `papers/Transactions on Emerging Telecommunications Technologies - 2019 - Hemanth - Performance analysis of the service periods of.pdf`
- **Performance Analysis and Energy Efficiency of MU- (OFDMA & MIMO) Based Hybrid MAC Protocol of IEEE 802.11ax WLANs**
  - *Authors:* Aparna Behara and T. G. Venkatesh
  - *Mapped Topic:* IEEE 802.11ax Hybrid Access (HA) Trigger Frame cycles, UORA backoff decrements by $N_{RA}$, 2D DTMC $\{s(t), b(t)\}$, MU-MIMO sounding airtime overhead $T_{csi}$, spatial Poisson process node distribution, and coverage probability $P_{cov}(r)$.
  - *Venue / File:* IEEE Transactions on Vehicular Technology, Vol. 72, No. 5, pp. 6474–6488 (2023) / `papers/Performance_Analysis_and_Energy_Efficiency_of_MU-_OFDMA_amp_MIMO_Based_Hybrid_MAC_Protocol_of_IEEE_802.11ax_WLANs.pdf`

### Papers in Archive
- **Performance evaluation of the QOS provisioning ability of IEEE 802.11e WLAN standard for multimedia traffic**
  - *Authors:* Venkata Sitaram A., T. G. Venkatesh, Arun George, R. Manivasakan, Bhasker Dappuri
  - *Mapped Topic:* IEEE 802.11e EDCA access categories (AC_VO, AC_VI, AC_BE, AC_BK) and QoS differentiation.
  - *Venue / File:* arXiv / TechRxiv preprint

### Conference Papers
- **A Simulation Study of the Contention Based Access Periods of the IEEE 802.11ad Hybrid MAC**
  - *Authors:* C. Hemanth and T. G. Venkatesh
  - *Mapped Topic:* Directional antenna alignment and CBAP contention in 60 GHz systems.
  - *Venue / File:* PGNet 2014
- **QoS Provisioning with Adaptive Backoff Algorithm for IEEE 802.11ac under Multipacket Reception**
  - *Authors:* Arun I. B, T. G. Venkatesh, and Bhasker Dappuri
  - *Mapped Topic:* Adaptive step decrements for multi-category EDCA in multi-packet reception channels.
  - *Venue / File:* CSNDSP 2014
- **Adaptive Backoff Algorithm for IEEE 802.11 DCF under MPR Wireless Channels**
  - *Authors:* Arun I. B and T. G. Venkatesh
  - *Mapped Topic:* Step-decrement backoff rules restoring the renewal property under MPR.
  - *Venue / File:* IEEE ICCCN 2013
- **Performance Study of High-Efficiency IEEE 802.11ax WLAN Standard using NS-3 Simulator**
  - *Authors:* Aparna Behara and T. G. Venkatesh
  - *Mapped Topic:* NS-3 simulation validation of UORA random access and scheduled access trade-offs.
  - *Venue / File:* IEEE CAMAD 2022
- **SIC and CSI-Based Random Channel Access Protocol for WLAN Supporting Multi Packet Transmissions**
  - *Authors:* Ankit Kumar Gupta, T. G. Venkatesh, and Navya Vuppalapati
  - *Mapped Topic:* Successive interference cancellation and channel sounding feedback for WLAN multi-packet access.
  - *Venue / File:* IEEE GCAIoT 2022

---

## Chapter 3: Advanced Features and QoS in IEEE 802.11
*Focus: EDCF/EDCA Access Categories, Multi-User EDCA (MU-EDCA), MAC frame aggregation (A-MSDU, A-MPDU, Multi-TID) and Block ACK, TXOP, Target Wake Time (TWT), BSS Coloring, Spatial Reuse (OBSS PD & PSR), Multi-Link Operation (MLO), Coordinated Multi-AP (JTX, CBF, Co-OFDMA), and Wi-Fi 8 (IEEE 802.11bn Ultra High Reliability).*

### Journals & Reference Monographs
- **WI-FI 6: Protocol and Network**
  - *Authors:* Susinder R. Gulasekaran and Sundar G. Sankaran
  - *Mapped Topic:* IEEE 802.11ax protocol architecture, Trigger Frame subfields, TWT service periods, and Spatial Reuse operation.
  - *Venue / File:* Artech House (2021) / `WIFI 7 and 8/`
- **Current Status and Directions of IEEE 802.11be, the Future Wi-Fi 7**
  - *Authors:* E. Khorov, I. Levitsky, and I. F. Akyildiz
  - *Mapped Topic:* IEEE 802.11be (Wi-Fi 7) 320 MHz channels, 4096-QAM, Multi-Link Operation (MLO), and restricted TWT.
  - *Venue / File:* IEEE Access, Vol. 8, pp. 88664–88688 (2020) / `WIFI 7 and 8/`
- **A Tutorial on Wi-Fi 8: The Journey to Ultra High Reliability**
  - *Authors:* Y. Karamysheva et al.
  - *Mapped Topic:* IEEE 802.11bn (Wi-Fi 8) Ultra High Reliability (UHR), Coordinated Spatial Reuse (Co-SR), Coordinated Beamforming (Co-BF), and Dynamic Subchannel Operation (DSO).
  - *Venue / File:* IEEE Communications Surveys & Tutorials (2025) / `WIFI 7 and 8/`
- **A Survey on IEEE 802.11bn Wi-Fi 8: Advantages of Ultra High Reliability for Next-Generation Wireless LANs**
  - *Authors:* Z. Ning, X. Wang, et al.
  - *Mapped Topic:* Deterministic latency guarantees, reliability enhancements, and PHY/MAC features of IEEE 802.11bn.
  - *Venue / File:* Survey paper (2026) / `WIFI 7 and 8/`

---

# Part II: Network Architectures and Paradigms

## Chapter 4: 5G Mobile Networks
*Focus: 5G New Radio (NR) flexible numerologies, initial access / RACH under directional beamforming, connection establishment, mmWave blockage dynamics, mobility, and eMBB/URLLC multiplexing.*

### Journals
- **A High Capacity Preamble Sequence for Random Access in 5G IoT Networks: Design and Analysis**
  - *Authors:* Lokesh Bommisetty and T. G. Venkatesh
  - *Mapped Topic:* High-capacity Zadoff-Chu preamble design, root sequence allocation, and multi-user preamble collision resolution for massive IoT in 5G NR.
  - *Venue / File:* IEEE Internet of Things Journal (2021) / `papers/A High Capacity Preamble Sequence for Random Access in 5G IoT Networks: Design and Analysis.pdf`
- **Performance Analysis of Connection Establishment Procedure Under Beamforming in 5G NR Networks**
  - *Authors:* Lokesh Bommisetty and T. G. Venkatesh
  - *Mapped Topic:* Directional beam sweeping, SS/PBCH block mapping, Random Access Preamble transmission under spatial analog beamforming, and connection latency.
  - *Venue / File:* IEEE Transactions on Mobile Computing, Vol. 22, No. 11, pp. 6690–6702 (2023) / `papers/Performance_Analysis_of_Connection_Establishment_Procedure_Under_Beamforming_in_5G_NR_Networks.pdf`
- **Performance Analysis of Random Access Mechanism in 5G Millimeter Wave Networks: Effect of Blockage, Shadowing and Mobility**
  - *Authors:* Lokesh Bommisetty, Sagar Pawar, and T. G. Venkatesh
  - *Mapped Topic:* 5G mmWave directional RACH, line-of-sight (LOS) to non-line-of-sight (NLOS) stochastic transition under human/dynamic blockage, and spatial mobility effects.
  - *Venue / File:* IEEE Access, Vol. 10, pp. 69651–69664 (2022) / `papers/Performance_Analysis_of_Random_Access_Mechanism_in_5G_Millimeter_Wave_Networks_Effect_of_Blockage_Shadowing_and_Mobility.pdf`
- **Modeling medium dense cellular network and evaluation of interference analysis**
  - *Authors:* Ravi Sankar Vaddi and T. G. Venkatesh
  - *Mapped Topic:* Stochastic geometry modeling of medium-density cellular base stations, inter-cell interference distributions, and Laplace functional analysis.
  - *Venue / File:* Transactions on Emerging Telecommunications Technologies (2023) / `papers/Transactions on Emerging Telecommunications Technologies - 2023 - Vaddi - Modeling medium dense cellular network and.pdf`

### Conference Papers
- **DQN-Based Joint Scheduling of eMBB and Massive URLLC in 5G Networks**
  - *Authors:* Rohan Desai, Indulekha K. P., and T. G. Venkatesh
  - *Mapped Topic:* Deep Reinforcement Learning for dynamic PRB puncturing and superposing URLLC mini-slots onto eMBB allocations.
  - *Venue / File:* IEEE Future Network World Forum 2025
- **Call Admission Control Schemes in Cellular Networks: A Comparative Study**
  - *Authors:* Santosh Kumar E. and T. G. Venkatesh
  - *Mapped Topic:* Guard channel CAC policies and handoff blocking probability analysis in mobile cellular networks.
  - *Venue / File:* JCSSE 2014

---

## Chapter 5: Personal Area Networks & Machine-to-Machine (M2M) Communication
*Focus: Short-range communication paradigms, M2M data collection networks, Dynamic Frame-Slotted ALOHA (DFSA), Multi-Packet Reception (MPR-DFSA), Karp-Upfal-Wigderson (KUW) algorithm bounds, energy efficiency, and pure ALOHA order statistics.*

### Journals
- **Performance Analysis of M2M Data Collection Networks Using Dynamic Frame-Slotted ALOHA**
  - *Authors:* Arun George and T. G. Venkatesh
  - *Mapped Topic:* Massive Machine-to-Machine (M2M) data collection, Dynamic Frame-Slotted ALOHA (DFSA), Karp-Upfal-Wigderson (KUW) inequality, average round bound $\mathbb{E}[R_n] \le e \ln n$, geometric backlog decay $\mathbb{E}[N_i] \approx n(1-e^{-1})^{i-1}$, IEEE 802.15.4 energy model, throughput lower bounds, and battery life maximization.
  - *Venue / File:* IEEE Transactions on Green Communications and Networking, Vol. 2, No. 2, pp. 493–501 (2018) / `papers/Performance_Analysis_of_M2M_Data_Collection_Networks_Using_Dynamic_Frame-Slotted_ALOHA.pdf`
- **Multi-packet reception dynamic frame-slotted ALOHA for IoT: Design and analysis**
  - *Authors:* Arun George and T. G. Venkatesh
  - *Mapped Topic:* IoT sensor networks with Multi-Packet Reception (MPR) capabilities under DFSA, optimal frame scaling factor $\beta_K$ ($\frac{1}{K} < \beta_K < \frac{1}{(K!)^{1/K}}$), success probability $B_K$, stopping time distribution, and maximum achievable throughput $\mathrm{TP}_K^* = B_K / \beta_K$.
  - *Venue / File:* Internet of Things, Elsevier, Vol. 11, 100256 (2020) / `papers/Multi-packet reception dynamic frame-slotted ALOHA for IoT: Design and analysis.pdf`
- **Order Statistics Based Analysis of Pure ALOHA in Channels with Multipacket Reception**
  - *Authors:* Arun I. B. and T. G. Venkatesh
  - *Mapped Topic:* Pure ALOHA with MPR, order statistics of packet arrival epochs, signal-to-interference ratio (SIR) distribution, capture effect, and spatial throughput scaling.
  - *Venue / File:* IEEE Communications Letters, Vol. 17, No. 10, pp. 1964–1967 (2013) / `papers/Order_Statistics_Based_Analysis_of_Pure_ALOHA_in_Channels_with_Multipacket_Reception.pdf`

### Papers in Archive
- **Minority Game based Content Distribution using Device-to-Device communication in IoT Networks**
  - *Authors:* Bhaswar Majumder, T. G. Venkatesh, and Y. Arun Kumar Reddy
  - *Mapped Topic:* Distributed game-theoretic content sharing across multi-hop D2D links in IoT underlay systems.
  - *Venue / File:* TechRxiv / arXiv preprint

---

## Chapter 6: Cognitive Radio Networks
*Focus: Dynamic Spectrum Access (DSA), spectrum sensing mechanisms (cooperative, quiet periods, heavy-tailed idle times), channel selection, and cognitive MAC protocols.*

### Journals
- **An analytical framework for cooperative cognitive radio network for spectrum leasing/sharing**
  - *Authors:* Bhasker Dappuri and T. G. Venkatesh
  - *Mapped Topic:* Primary-secondary spectrum leasing contracts, cooperative relaying, and reward-maximization MAC frameworks.
  - *Venue / File:* Computer Networks, Elsevier (2018) / `papers/An analytical framework for cooperative cognitive radio network for spectrum leasingsharing.pdf`
- **Analysis of Quiet Period Scheduling in QP-CSMA-CA Cognitive Radio MAC Protocol**
  - *Authors:* S. Senthilmurugan and T. G. Venkatesh
  - *Mapped Topic:* Quiet Period (QP) duration optimization, secondary user sensing intervals, and collision probability bounds with primary users.
  - *Venue / File:* Wireless Personal Communications, Vol. 92, No. 4, pp. 1625–1637 (2017) / `papers/Analysis of Quiet Period Scheduling in QP-CSMA-CA Cognitive Radio MAC Protocol.pdf`
- **Channel Selection Algorithm for Cognitive Radio Networks with Heavy-Tailed Idle Times**
  - *Authors:* S. Senthilmurugan and T. G. Venkatesh
  - *Mapped Topic:* Pareto / heavy-tailed primary user idle channel distribution, residual channel holding times, and optimal secondary channel ranking.
  - *Venue / File:* IEEE Transactions on Mobile Computing, Vol. 16, No. 5, pp. 1258–1269 (2017) / `papers/Channel_Selection_Algorithm_for_Cognitive_Radio_Networks_with_Heavy-Tailed_Idle_Times.pdf`

- **Optimal Channel Sensing Strategy for Cognitive Radio Networks With Heavy-Tailed Idle Times**
  - *Authors:* S. Senthilmurugan and T. G. Venkatesh
  - *Mapped Topic:* Stopping-time formulation for primary channel vacancy detection under non-exponential, heavy-tailed idle durations.
  - *Venue / File:* IEEE Transactions on Cognitive Communications and Networking, Vol. 3, No. 1, pp. 26–36 (2017) / `papers/Optimal_Channel_Sensing_Strategy_for_Cognitive_Radio_Networks_With_Heavy-Tailed_Idle_Times.pdf`
- **Design and Performance Analysis of Cognitive WLAN MAC Protocol**
  - *Authors:* Bhasker Dappuri and T. G. Venkatesh
  - *Mapped Topic:* Cooperative basic access vs. RTS/CTS adaptation in opportunistic secondary WLAN deployments.
  - *Venue / File:* Wireless Networks, Springer (2016) / `papers/Design_and_Performance_Analysis_of_Cognitive_WLAN_MAC_Protocol.pdf`
- **Design and Performance Analysis of Multichannel MAC Protocol for Cognitive WLAN**
  - *Authors:* Bhasker Dappuri and T. G. Venkatesh
  - *Mapped Topic:* Multichannel rendezvous, dedicated vs. split control channel architectures in cognitive WLANs.
  - *Venue / File:* IET Networks (2017) / `papers/Design_and_Performance_Analysis_of_Multichannel_MAC_Protocol_for_Cognitive_WLAN.pdf`

### Conference Papers
- **Preemptive Priority Mechanism with Hybrid Spectrum Sensing for Cognitive Radio Networks**
  - *Authors:* Bhasker Dappuri, Madhu Babu Sikha, and T. G. Venkatesh
  - *Mapped Topic:* Preemptive resume priority (PRP) queueing under hybrid energy detection and cyclostationary feature sensing.
  - *Venue / File:* IEEE ICACCI 2017
- **IEEE 802.11 DCF MAC Protocol for Cognitive Radio Networks: Cooperative Basic Access Vs RTS/CTS**
  - *Authors:* Bhasker Dappuri and T. G. Venkatesh
  - *Mapped Topic:* Contention overhead and hidden node mitigation in cognitive WLANs.
  - *Venue / File:* ISCIT 2014
- **A MAC protocol for implementing differential services over Cognitive Radio Networks**
  - *Authors:* Vivin Thomas, T. G. Venkatesh, and Bhasker Dappuri
  - *Mapped Topic:* Priority differentiation and QoS support in dynamic spectrum sharing.
  - *Venue / File:* IEEE CONECCT 2014
- **Performance analysis of Cooperative Cognitive Distributed MAC Protocol with Full duplex links**
  - *Authors:* S. Senthilmurugan and T. G. Venkatesh
  - *Mapped Topic:* Full-duplex secondary links for concurrent transmission and primary user sensing.
  - *Venue / File:* MACOM 2013
- **MAC protocols for Cognitive Radio Networks with passive and Active primary users**
  - *Authors:* Bhasker Dappuri, T. G. Venkatesh, and Vivin Thomas
  - *Mapped Topic:* Active primary feedback vs. passive listen-before-talk secondary protocols.
  - *Venue / File:* WCSP 2013

---

## Chapter 7: Heterogeneous Networks (HetNets)
*Focus: Macrocells, small cells, internetworking, mobile data offloading (on-the-spot, delayed, QoS-guaranteed), user balking, and traffic steering.*

### Journals
- **Design and Performance Analysis of Prioritized On-the-Spot Mobile Data Offloading Scheme**
  - *Authors:* Anusree Ajith and T. G. Venkatesh
  - *Mapped Topic:* Multi-priority on-the-spot offloading from cellular macrocells to Wi-Fi small cells, preemption mechanisms, and non-preemptive queueing models.
  - *Venue / File:* IEEE Transactions on Vehicular Technology, Vol. 67, No. 8, pp. 7644–7657 (2018) / `papers/Design and Performance Analysis of Prioritized On-the-Spot Mobile Data Offloading Scheme.pdf`
- **Delayed mobile data offloading scheme for quality of service traffic: Design and analysis**
  - *Authors:* Anusree Ajith and T. G. Venkatesh
  - *Mapped Topic:* Delay tolerance deadlines, delayed offloading with QoS constraints, and cellular cost minimization.
  - *Venue / File:* IET Networks, Vol. 10, Iss. 3, pp. 119–130 (2021) / `papers/IET Networks - 2021 - Ajith - Delayed mobile data offloading scheme for quality of service traffic Design and analysis.pdf`
- **QoE Enhanced Mobile Data Offloading With Balking**
  - *Authors:* Anusree Ajith and T. G. Venkatesh
  - *Mapped Topic:* User psychology and impatience modeling via state-dependent balking probability $b_{(n,k)}$ in regenerative alternating renewal queues.
  - *Venue / File:* IEEE Communications Letters, Vol. 21, No. 5, pp. 1143–1146 (2017) / `papers/QoE_Enhanced_Mobile_Data_Offloading_With_Balking.pdf`

### Conference Papers
- **Mobile Data Offloading for Streaming-Class Traffic with QoS Guarantee**
  - *Authors:* Anusree Ajith and T. G. Venkatesh
  - *Mapped Topic:* Streaming video buffer dynamics during cellular-to-WLAN offloading transitions.
  - *Venue / File:* WTS 2016 / IJITN

---

## Chapter 8: Internet of Things & Low-Power Wide-Area Networks
*Focus: Narrowband IoT (NB-IoT), random access and Access Class Barring (ACB), IEEE 802.15.4e Time Slotted Channel Hopping (TSCH), 6TiSCH dynamic scheduling, and M2M Dynamic Frame-Slotted ALOHA (DFSA).*

### Journals
- **Performance evaluation of random access in narrow band Internet of Things**
  - *Authors:* Chaturasan Ramineni, T. G. Venkatesh, and Lokesh Bommisetty
  - *Mapped Topic:* NB-IoT Random Access Channel (NPRACH), Multi-Band Multi-Carrier Slotted ALOHA model, 3 Coverage Enhancement (CE) levels (CE 0, CE 1, CE 2), 3D DTMC $(i, j, k)$ state analysis, CE migration dynamics, sub-carrier allocation optimization, and throughput/collision probability derivations.
  - *Venue / File:* Computer Networks, Elsevier, Vol. 218, 109399 (2022) / `papers/Performance evaluation of random access in narrow band Internet of Things.pdf`
- **Impact of access class barring in narrow band internet of things**
  - *Authors:* Chaturasan Ramineni and T. G. Venkatesh
  - *Mapped Topic:* NB-IoT RACH overload mitigation, Access Class Barring (ACB) vs. Extended Access Barring (EAB), SIB-2 broadcast parameter tuning (barring factor, barring time), access success probability, and access latency reduction.
  - *Venue / File:* IET Wireless Sensor Systems, Vol. 9, Iss. 6, pp. 399–404 (2019) / `papers/IET Wireless Sensor Systems - 2019 - Ramineni - Impact of access class barring in narrow band internet of things.pdf`
- **Dynamic Programming based Low-Latency Schedule (DPLLS) for 6TiSCH networks**
  - *Authors:* Lokesh Bommisetty and T. G. Venkatesh
  - *Mapped Topic:* Industrial IoT, IEEE 802.15.4e TSCH, 6TiSCH protocol stack, RPL DODAG tree, Maximum Weight Independent Set (MWIS) via recursive Dynamic Programming, Generalised Conflict Graph (GCG) eliminating primary and secondary sum-interference, low-latency block scheduling, and reliability retransmission replication.
  - *Venue / File:* Ad Hoc Networks, Elsevier, Vol. 124, 102708 (2022) / `papers/Dynamic Programming based Low-Latency Schedule (DPLLS) for 6TiSCH networks.pdf`
- **Contention-Based Proportional Fairness (CBPF) Transmission Scheme for Time Slotted Channel Hopping Networks**
  - *Authors:* Lokesh Bommisetty and T. G. Venkatesh
  - *Mapped Topic:* TSCH Multichannel Slotted ALOHA modeling, Contention-Based Proportional Fairness (CBPF), convex optimization with KKT conditions, non-identical transmission indicators via characteristic functions and IDFT, throughput, Pollaczek-Khinchin M/G/1 queueing delay, and energy consumption per successful packet.
  - *Venue / File:* IEEE Transactions on Industrial Informatics, Vol. 19, No. 2, pp. 1289–1298 (2023) / `papers/Contention-Based_Proportional_Fairness_CBPF_Transmission_Scheme_for_Time_Slotted_Channel_Hopping_Networks.pdf`
- **Performance Analysis of M2M Data Collection Networks Using Dynamic Frame-Slotted ALOHA**
  - *Authors:* Arun George and T. G. Venkatesh
  - *Mapped Topic:* Massive Machine-to-Machine (M2M) data collection, Dynamic Frame-Slotted ALOHA (DFSA), optimal frame length adaptation, backlog estimation, and energy efficiency.
  - *Venue / File:* IEEE Transactions on Green Communications and Networking, Vol. 2, No. 2, pp. 493–501 (2018) / `papers/Performance_Analysis_of_M2M_Data_Collection_Networks_Using_Dynamic_Frame-Slotted_ALOHA.pdf`
- **Multi-packet reception dynamic frame-slotted ALOHA for IoT: Design and analysis**
  - *Authors:* Arun George and T. G. Venkatesh
  - *Mapped Topic:* IoT sensor networks with Multi-Packet Reception (MPR) capabilities under DFSA, frame length Markov decision models, and energy-throughput trade-offs.
  - *Venue / File:* Internet of Things, Elsevier, Vol. 11, 100256 (2020) / `papers/Multi-packet reception dynamic frame-slotted ALOHA for IoT: Design and analysis.pdf`

### Conference Papers
- **Efficiency analysis of M2M Data Collection networks using Multipacket Reception in Frame-Slotted ALOHA**
  - *Authors:* Arun George and T. G. Venkatesh
  - *Mapped Topic:* Energy efficiency and throughput bounds of MPR-enabled M2M data collection under DFSA.
  - *Venue / File:* IEEE WCNC 2016
- **BIOS: Biogeography Inspired Optimal Scheduling Algorithm for TSCH Networks**
  - *Authors:* Lokesh Bommisetty and T. G. Venkatesh
  - *Mapped Topic:* Metaheuristic Biogeography-Based Optimization (BBO) for habitat migration and slotframe scheduling in 6TiSCH networks.
  - *Venue / File:* IEEE APCC 2021
- **Phasic Policy Gradient Based Resource Allocation for Industrial Internet of Things**
  - *Authors:* Lokesh Bommisetty and T. G. Venkatesh
  - *Mapped Topic:* Reinforcement learning via Phasic Policy Gradient (PPG) separating policy optimization and auxiliary value function training in TSCH.
  - *Venue / File:* IEEE CCNC 2022

---

## Chapter 9: Sensor Area Networks and Age of Information
*Focus: Information freshness metrics (Average AoI, Peak AoI), FCFS vs. LCFS disciplines with preemption, Stochastic Hybrid Systems (SHS), Proactive Obsolete Packet Management (POPMAN) in heterogeneous parallel servers, and multi-hop / multi-source priority sensor networks.*

### Journals
- **Age of Information Analysis for Queueing Systems With Proactive Obsolete Packet Management: Multi-Hop, Multi-Source, and Priority Mechanisms**
  - *Authors:* Y. Arun Kumar Reddy and T. G. Venkatesh
  - *Mapped Topic:* Information freshness, Peak and Average Age of Information (AoI), Proactive Obsolete Packet Management (POPMAN), buffer flush mechanisms in multi-hop, multi-source, and preemptive heterogeneous server queues.
  - *Venue / File:* IEEE Transactions on Mobile Computing (2024) / `papers/Age_of_Information_Analysis_for_Queueing_Systems_With_Proactive_Obsolete_Packet_Management_Multi-Hop_Multi-Source_and_Priority_Mechanisms.pdf`

### Papers in Archive
- **Proactive obsolete packet management based analysis of age of information for lcfs heterogeneous queueing system**
  - *Authors:* Y. Arun Kumar Reddy and T. G. Venkatesh
  - *Mapped Topic:* LCFS queuing disciplines with proactive packet dropping under heterogeneous servers.
  - *Venue / File:* TechRxiv (2024) / `papers/Proactive Obsolete Packet Management based analysis of Age of Information for LCFS Heterogeneous Queueing System Y. Arun Kumar Reddy, T G Venkatesh.pdf`
- **Age of information of an fcfs queueing system in heterogeneous servers with proactive obsolete packet management**
  - *Authors:* Y. Arun Kumar Reddy and T. G. Venkatesh
  - *Mapped Topic:* FCFS queueing analysis with POPMAN discarding outdated status updates.
  - *Venue / File:* TechRxiv preprint
- **Relative freshness stochastic hybrid systems markov chain (rf-shs-mc) model for the study of age of information**
  - *Authors:* Y. Arun Kumar Reddy and T. G. Venkatesh
  - *Mapped Topic:* Stochastic Hybrid Systems (SHS) with continuous state aging and discrete jumping boundaries.
  - *Venue / File:* TechRxiv preprint

### Conference Papers
- **Relative Freshness Stochastic Hybrid Systems Markov Chain (RF-SHS-MC) model for the study of Age of Information**
  - *Authors:* Y. Arun Kumar Reddy and T. G. Venkatesh
  - *Mapped Topic:* RF-SHS-MC model for status freshness evaluation in wireless sensor networks.
  - *Venue / File:* IEEE Future Network World Forum 2025

---

## Chapter 10: Vehicular Networks
*Focus: VANETs, IEEE 802.11p/WAVE safety message dissemination, LTE-V2X (Mode 3 & Mode 4 autonomous resource allocation), NR-V2X (Mode 1 & Mode 2), Integrated Sensing and Communication (ISAC), and Reconfigurable Intelligent Surface (RIS) assisted full-duplex V2X.*

### Conference Papers
- **Evaluation of Traffic-Safety features of WAVE Protocol for Vehicular Ad-hoc Networks**
  - *Authors:* T. G. Venkatesh and Dhananjay Kumar
  - *Mapped Topic:* IEEE 802.11p WAVE safety beacon dissemination delay, channel switching, and packet reception ratios.
  - *Venue / File:* IEEE WiSPNET 2019
- **Performance Analysis of the Radio Access Technologies (RAT) of Vehicular Communications**
  - *Authors:* Bhargavi Toparapu, Aparna Behara, Lokesh Bommisetty, and T. G. Venkatesh
  - *Mapped Topic:* Comparative evaluation of DSRC (802.11p), LTE-V2X sidelink, and NR-V2X physical layer performance under vehicular mobility.
  - *Venue / File:* IEEE ANTS 2022
- **Optimal Resource Allocation in NR-V2X: A Deep Reinforcement Learning Approach for Aperiodic Traffic in Vehicular Networks**
  - *Authors:* Indulekha K. P. and T. G. Venkatesh
  - *Mapped Topic:* Deep Reinforcement Learning for NR-V2X Mode 2 sidelink autonomous resource allocation under bursty aperiodic traffic.
  - *Venue / File:* IEEE IoTaIS 2024
- **Dynamic Resource and Power Allocation strategy for ISAC-Aided 5G V2X Networks using Reinforcement learning**
  - *Authors:* Indulekha K. P. and T. G. Venkatesh
  - *Mapped Topic:* Dual-functional radar-communication (DFRC) waveforms, radar target tracking accuracy, and V2X throughput maximization via Q-learning.
  - *Venue / File:* IEEE ANTS 2024
- **RIS-Assisted Full Duplex MAC Protocol for NR-V2X with ML-Driven QoS Prediction**
  - *Authors:* Indulekha K. P. and T. G. Venkatesh
  - *Mapped Topic:* Intelligent reflecting surfaces (RIS) for millimeter-wave vehicular blockage bypass combined with full-duplex transmission and LSTM QoS prediction.
  - *Venue / File:* IEEE Future Network World Forum 2025

---

# Part III: Advanced Optimization and Modelling

## Chapter 11: Cross-Layer Design, Full-Duplex, and SIC
*Focus: Physical-MAC layer coupling, Successive Interference Cancellation (SIC) with signal transmission diversity, constellation-based full duplex (C-FD MAC), and synchronized full duplex (SM-FD MAC).*

### Journals
- **C-FD MAC: Constellation based Full-Duplex MAC protocol**
  - *Authors:* Surya Bhushan Dwivedi, Ankit Kumar Gupta, and T. G. Venkatesh
  - *Mapped Topic:* Constellation mapping, instant link discovery, channel sounding embedding in control signaling, and self-interference cancellation overhead minimization.
  - *Venue / File:* IEEE Access (2022) / `papers/C-FD MAC: Constellation based Full-Duplex MAC protocol.pdf`
- **Design and performance evaluation of successive interference cancellation based Slotted Aloha MAC protocol**
  - *Authors:* Ankit Kumar Gupta and T. G. Venkatesh
  - *Mapped Topic:* Closed-form packet decoding probabilities via order statistics under fixed and random node topologies, MGF/Laplace inversions, optimal offered load ($G_{opt} pprox 2.64$), and imperfect CSI/SIC impairments.
  - *Venue / File:* Physical Communication, Elsevier, Vol. 55, 101910 (2022) / `papers/Design and performance evaluation of successive interference cancellation based Slotted Aloha MAC protocol.pdf`
- **Order Statistics Based Analysis of Pure ALOHA in Channels with Multipacket Reception**
  - *Authors:* Arun I. B and T. G. Venkatesh
  - *Mapped Topic:* Exact closed-form pure ALOHA throughput with collision polynomial coefficients, order statistics on vulnerable interval $[-1, 1]$, and MPR upper bound $S \le K/e$.
  - *Venue / File:* IEEE Communications Letters, Vol. 17, No. 10, pp. 1964–1967 (2013) / `papers/Order_Statistics_Based_Analysis_of_Pure_ALOHA_in_Channels_with_Multipacket_Reception.pdf`
- **Signal transmission diversity based successive interference cancellation-slotted aloha**
  - *Authors:* Ankit Kumar Gupta and T. G. Venkatesh
  - *Mapped Topic:* Multi-slot packet replica transmission, iterative forward-backward graph-based cancellation, baseband collision buffering, and capacity doubling in ALOHA.
  - *Venue / File:* Ad Hoc Networks, Elsevier, Vol. 158, 103482 (2024) / `papers/Signal transmission diversity based successive interference cancellation-slotted aloha.pdf`

---

## Chapter 12: Game Theory Applications
*Focus: Non-cooperative strategic games, Nash equilibrium, utility and pricing incentives, Minority Game (MG) framework for mobile data offloading (exponential learning, target pricing), crowd-anticrowd theory, contention window adaptation games, and power control games.*

### Journals
- **Mobile data offloading based on minority game theoretic framework**
  - *Authors:* Bhaswar Majumder and T. G. Venkatesh
  - *Mapped Topic:* Minority Game (MG) framework for distributed network selection between cellular and Wi-Fi, inductive reinforcement learning, and price incentive mechanisms.
  - *Venue / File:* Wireless Networks, Springer, Vol. 28, pp. 2967–2982 (2022) / `papers/Mobile data offloading based on minority game theoretic framework.pdf`

### Papers in Archive
- **Minority-Game Multi-packet-reception medium access protocol: Design and analysis**
  - *Authors:* Bhaswar Majumder, T. G. Venkatesh, and Y. Arun Kumar Reddy
  - *Mapped Topic:* Multi-packet reception channels regulated by inductive minority game strategies.
  - *Venue / File:* arXiv / TechRxiv preprint

### Conference Papers
- **Wireless MAC Protocol based on Crowd Anticrowd Theory**
  - *Authors:* Bhaswar Majumder, T. G. Venkatesh, and Navya Vuppalapati
  - *Mapped Topic:* Crowd-anticrowd statistical physics modeling of agent clustering in random access contention.
  - *Venue / File:* IEEE ICACCE 2020

---

## Chapter 13: Machine Learning Applications
*Focus: Reinforcement Learning (RL) and Multi-Armed Bandit (MAB) paradigms in MAC design, Phasic Policy Gradient (PPG) for IEEE 802.15.4e TSCH, Contextual Multi-Armed Bandits (LinUCB) for 5G NR initial access & adaptive numerology under blockage, Deep Q-Networks (DQN / DDQN), and Automatic Modulation Classification.*

### Journals
- **Resource Allocation in Time Slotted Channel Hopping (TSCH) Networks Based on Phasic Policy Gradient Reinforcement Learning**
  - *Authors:* Lokesh Bommisetty and T. G. Venkatesh
  - *Mapped Topic:* Phasic Policy Gradient (PPG) architecture for TSCH, policy network vs. auxiliary value network training, reward shaping, and convergence acceleration over PPO.
  - *Venue / File:* Internet of Things, Elsevier, Vol. 19, 100522 (2022) / `papers/Resource Allocation in Time Slotted Channel Hopping (TSCH) Networks Based on Phasic Policy Gradient Reinforcement Learning.pdf`
- **Contextual Bandit Based Adaptive Numerology for Initial Access in 5G NR Networks**
  - *Authors:* Lokesh Bommisetty and T. G. Venkatesh
  - *Mapped Topic:* Linear Upper Confidence Bound (LinUCB) contextual multi-armed bandit algorithm for dynamically selecting 5G NR subcarrier spacing (SCS) and beam sweep patterns under fluctuating blockage environments.
  - *Venue / File:* IEEE Transactions on Cognitive Communications and Networking (2023) / `papers/Contextual Bandit Based Adaptive Numerology for Initial Access in 5G NR Networks.pdf`

### Conference Papers
- **Deep Learning-Based Hybrid Models for Automatic Modulation Classification**
  - *Authors:* Rashmi Prajapati, Rohan Desai, T. G. Venkatesh, and Indulekha K. P.
  - *Mapped Topic:* Residual neural networks (ResNet) and CNN-LSTM architectures for automatic modulation classification (AMC) in low-SNR wireless channels.
  - *Venue / File:* IEEE CINS 2024

---

## Chapter 14: Network on Chip
*Focus: Multi-core chip architectures, wireless network-on-chip (WNoC), cache reuse distance profiles (L1 to L2), 3D-stacked memories, Near-Memory Processing (NMP), Memory Centric Networks (MCN), and Multi-Armed Bandit task allocation.*

### Journals
- **Analytical Derivation of Concurrent Reuse Distance Profile for Multi-Threaded Application Running on Chip Multi-Processor**
  - *Authors:* Murali Dadi and T. G. Venkatesh
  - *Mapped Topic:* Concurrent reuse distance (CRD) profiles, Markov chain cache models, and inter-thread cache interference on chip multi-processors (CMPs).
  - *Venue / File:* IEEE Access, Vol. 8 (2020) / `papers/Analytical_Derivation_of_Concurrent_Reuse_Distance_Profile_for_Multi-Threaded_Application_Running_on_Chip_Multi-Processor.pdf`
- **Analytical Miss Rate Calculation of L2 Cache from the RD Profile of L1 Cache**
  - *Authors:* Murali Dadi and T. G. Venkatesh
  - *Mapped Topic:* Analytical transfer functions projecting L1 cache filtered reference traces to L2 cache miss rates.
  - *Venue / File:* IEEE Transactions on Very Large Scale Integration (VLSI) Systems (2021) / `papers/Analytical_Miss_Rate_Calculation_of_L2_Cache_from_the_RD_Profile_of_L1_Cache.pdf`
- **Design and implementation of congestion aware router for network-on-chip**
  - *Authors:* Vijaya Bhaskar Adusumilli and T. G. Venkatesh
  - *Mapped Topic:* Congestion-aware deflection routing, buffer status signaling, and throughput starvation mitigation in 2D mesh NoCs.
  - *Venue / File:* Microprocessors and Microsystems, Elsevier (2020) / `papers/Design and implementation of congestion aware router for network-on-chip.pdf`
- **Performance analysis of network-on-chip in many-core processors**
  - *Authors:* Vijaya Bhaskar Adusumilli and T. G. Venkatesh
  - *Mapped Topic:* Multi-class queueing network analysis of NoC topologies under synthetic and realistic traffic traces.
  - *Venue / File:* Journal of Parallel and Distributed Computing (JPDC), Elsevier, Vol. 147, pp. 196–208 (2021) / `papers/Performance analysis of network-on-chip in many-core processors.pdf`
- **Performance investigation of packet-based communication in 3D-memories**
  - *Authors:* Shubhang Pandey and T. G. Venkatesh
  - *Mapped Topic:* Through-Silicon Via (TSV) vertical bus models, thermal constraints, and packetized interconnects in 3D-stacked memories.
  - *Venue / File:* The Journal of Supercomputing, Vol. 78, pp. 19070–19096 (2022) / `papers/Performance investigation of packet-based communication in 3D-memories.pdf`
- **Traffic Characterization Based Stochastic Modelling of Network-on-Chip**
  - *Authors:* Vijaya Bhaskar Adusumilli and T. G. Venkatesh
  - *Mapped Topic:* Self-similar and Markov modulated Poisson process (MMPP) traffic modeling for on-chip network routers.
  - *Venue / File:* IEEE Transactions on Computers, Vol. 72, No. 4, pp. 1032–1043 (2023) / `papers/Traffic_Characterization_Based_Stochastic_Modelling_of_Network-on-Chip.pdf`
- **Multi Armed Bandit based Resource Allocation in Near Memory Processing Architectures**
  - *Authors:* Shubhang Pandey and T. G. Venkatesh
  - *Mapped Topic:* Online reinforcement learning / MAB allocation of memory-intensive compute kernels across heterogeneous NMP compute units.
  - *Venue / File:* arXiv:2312.07640 (2023) / `papers/Multi Armed Bandit based Resource Allocation in Near Memory Processing Architectures Shubhang Pandey and T G Venkatesh.pdf`

### Papers in Archive
- **Performance Study of Partitioned Caches in Asymmetric Multi-Core Processors**
  - *Authors:* Murali Dadi, Shubhang Pandey, Aparna Behara, and T. G. Venkatesh
  - *Mapped Topic:* Way-partitioning and cache quota enforcement in asymmetric multi-core systems.
  - *Venue / File:* arXiv preprint
- **MRCN: Enhanced Coherence Mechanism for Near Memory Processing Architectures**
  - *Authors:* Amit Kumar Kabat, Shubhang Pandey, and T. G. Venkatesh
  - *Mapped Topic:* Memory-Centric Coherence protocols for 3D Near-Memory Processing.
  - *Venue / File:* arXiv preprint

### Conference Papers
- **Performance Evaluation of High Bandwidth Memory for HPC Workloads**
  - *Authors:* Amit Kumar Kabat, Shubhang Pandey, and T. G. Venkatesh
  - *Mapped Topic:* High Bandwidth Memory (HBM2) latency and bandwidth saturation under scientific workloads.
  - *Venue / File:* IEEE SOCC 2022
- **SOBLPM: Stochastic optimization Based Link Power Management for 3D-Stacked Memories**
  - *Authors:* Shubhang Pandey and T. G. Venkatesh
  - *Mapped Topic:* Dynamic voltage and frequency scaling (DVFS) and link power management in TSV networks.
  - *Venue / File:* IEEE DCAS 2022
- **Exploration of Design Optimizations for STTMRAM as L1 Cache**
  - *Authors:* Shubhang Pandey, T. G. Venkatesh, and Naresh Ramavath
  - *Mapped Topic:* Spin-Transfer Torque MRAM non-volatile cache design and write-energy mitigation.
  - *Venue / File:* IEEE SCOReD 2021
- **A study of the effect of virtual channels on the performance of Network-on-Chip**
  - *Authors:* Vijaya Bhaskar Adusumilli and T. G. Venkatesh
  - *Mapped Topic:* Virtual channel buffer allocation, head-of-line blocking elimination in NoC routers.
  - *Venue / File:* IEEE SCOReD 2015

---

## Chapter 15: Analytical Techniques for MAC Performance Evaluation
*Focus: Analytical modeling methodologies, Software-Defined Networks (SDN) under non-stationary conditions, hybrid IP/SDN candidate selection algorithms, and stochastic stability modeling.*

### Journals
- **Candidate Selection Algorithms for Hybrid IP SDN Networks With Multi-Link Failures**
  - *Authors:* Navya Vuppalapati and T. G. Venkatesh
  - *Mapped Topic:* Integer linear programming (ILP) and heuristic candidate selection algorithms for incremental SDN router deployment tolerating multi-link failures.
  - *Venue / File:* IEEE Transactions on Network and Service Management (2023) / `papers/Candidate_Selection_Algorithms_for_Hybrid_IP_SDN_Networks_With_Multi-Link_Failures.pdf`
- **Minimum Candidate Selection Algorithm for Hybrid IP SDN Networks With Single Link Failures**
  - *Authors:* Navya Vuppalapati and T. G. Venkatesh
  - *Mapped Topic:* Greedy candidate selection algorithms for single link failure survivability in hybrid IP/SDN backbones.
  - *Venue / File:* IEEE Networking Letters, Vol. 3, No. 3, pp. 138–142 (2021) / `papers/Minimum_Candidate_Selection_Algorithm_for_Hybrid_IP_SDN_Networks_With_Single_Link_Failures.pdf`
- **Modeling & analysis of software defined networks under non-stationary conditions**
  - *Authors:* Navya Vuppalapati and T. G. Venkatesh
  - *Mapped Topic:* Transient queueing models, fluid flow approximations, and time-dependent controller response in non-stationary SDN networks.
  - *Venue / File:* Peer-to-Peer Networking and Applications, Vol. 14, pp. 1174–1189 (2021) / `papers/Modeling & analysis of software defined networks under non-stationary conditions.pdf`
- **Voltage stability – Case study of saddle node bifurcation with stochastic load dynamics**
  - *Authors:* R. C. Kumaran, K. S. Swarup, and T. G. Venkatesh
  - *Mapped Topic:* Stochastic differential equations (SDE), Langevin formulations, and saddle-node bifurcations.
  - *Venue / File:* Electrical Power and Energy Systems, Elsevier, Vol. 33, pp. 1384–1388 (2011) / `papers/Voltage stability – Case study of saddle node bifurcation with stochastic load dynamics.pdf`
- **Damped bistable system driven by colored noise: A digital simulation study**
  - *Authors:* Chitralekha Mahanta and T. G. Venkatesh
  - *Mapped Topic:* Non-Markovian noise processes, colored noise driving potential systems, and escape times.
  - *Venue / File:* Physical Review E, Vol. 58, No. 4, pp. 4141–4146 (1998) / `papers/amped bistable system driven by colored noise: A digital simulation study.pdf`

### Conference Papers
- **A Class of Candidate Selection Algorithms for Hybrid IP/SDN to Tolerate Single Bidirectional Link Failures with Budget Constraints**
  - *Authors:* Navya Vuppalapati, T. G. Venkatesh, and Ankit Kumar Gupta
  - *Mapped Topic:* Budget-constrained SDN node upgrades for bidirectional survivability.
  - *Venue / File:* IEEE GCAIoT 2022
- **Traffic Modeling & Characterization of Software Defined Networks**
  - *Authors:* Navya Vuppalapati, T. G. Venkatesh, and Bhaswar Majumder
  - *Mapped Topic:* OpenFlow control plane queueing and packet-in message arrival characterization.
  - *Venue / File:* IEEE ICACCE 2020
- **Performance Evaluation of MAC protocols for Next Generation Wireless Networks using SIMPY**
  - *Authors:* C. Hemanth, T. G. Venkatesh, and Sriram V. Iyer
  - *Mapped Topic:* Discrete-event simulation methodology for wireless MAC protocols using SimPy.
  - *Venue / File:* SciPy India 2010

---

## Summary of Excluded Items (Non-Monograph / Out-of-Scope)
The following candidate entries were filtered out as they do not belong to wireless networking, MAC protocols, or queueing/analytical computer architecture:
1. *Cybersecurity / IDS:*
   - Rohan Desai, T. G. Venkatesh, "Network Intrusion Detection Through Machine Learning with Efficient Feature Selection" (COMSNETS 2023)
   - Rohan Desai, T. G. Venkatesh, "Robust Network Intrusion Detection Systems for Outlier Detection" (IEEE CAMAD 2022)
2. *General Machine Learning / Optimization:*
   - Deddy Jobson, T. G. Venkatesh, "Dimensionality Reduction Techniques to Aid Parallelization of Machine Learning Algorithms" (I2CT 2022)
3. *Power Systems / Grid Dynamics:*
   - Kumaran R. C., Swarup K. S., Venkatesh T. G., "Simulation of SMIB power system with stochastic load" (PMAPS 2010)
   - Kumaran R. C., Venkatesh T. G., Swarup K. S., "Power System Stability Analysis Using Perturbation Technique" (NSC 2008)
4. *Software / Industry Talks & Legacy 1991 Neural Network Papers:*
   - T. G. Venkatesh, JavaOne 2001 BOF Talk on Java Media Framework
   - T. G. Venkatesh, Adriatico 1995 Invited Lecture on Bistability and Colored Noise
   - T. G. Venkatesh, L. M. Patnaik, "Associative memory design: Fokker-Planck formalism" (1991)
   - T. G. Venkatesh, L. M. Patnaik, "Unlearning in feed-forward neural network" (TENCON 1991)
   - L. M. Patnaik, T. G. Venkatesh, "Trends in AI architecture" (1991)
   - L. M. Patnaik et al., "Transputers in industrial automation" (1991)
