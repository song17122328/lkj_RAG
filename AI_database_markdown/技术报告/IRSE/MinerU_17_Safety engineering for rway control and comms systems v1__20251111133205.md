# Safety Engineering for Railway Control & Communications Systems

An introductory guide for candidates taking Module A of the IRSE Professional Examination

R Short

February 2021

# Part 1: Safety Principles

This part should be treated as an addendum to the item in the Module A reading list entitled "Back to Basics - Principles of Railway Safety Engineering, IRSE News, Issue 267, June 2020" which explains the identification and analysis of hazards and risks.

# Hazard, Risk and Safety Requirements

It is essential to derive a complete and correct specification of safety requirements as part of system development.

Systematic identification of hazards generally involves two phases:

- an empirical phase (exploiting past experience, e.g. checklists)  
- a deductive phase (proactive forecasting, e.g. brain-storming, structured what-if studies, HAZOP, FMEA).

Hazard Control consists of a number of activities which can be summarized as follows:

- define the safety assumptions and system functions related to the defined hazards  
- define the system architecture and allocate system functions within the architecture (technical solution) to meet the safety requirements including the defined THRs  
- perform the hazard analysis (or causal analysis), to evaluate the possible causes of hazards  
- determine the safety integrity requirements for the functions of the system  
complete the safety requirements specification  
- identify potential new hazards arising out of the system design

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/26260d8a-8313-4d7f-8953-d0e2817fe234/0b1972f541e59e86937be08b3d889cbdf6ddbaf829875b366bb2b645e173e8b7.jpg)  
Process Overview

# Risk Acceptance

Risk acceptance criteria depend on national or international legislative requirements.

The Common Safety Method (CSM) promoted by the European Rail Agency (ERA) recognises three risk acceptance principles:

>use of a code of practice;  
>use of a similar system as a reference;  
> explicit risk estimation (here the ERA says “The acceptability of the estimated risks shall be evaluated using risk acceptance criteria either derived from or based on legal requirements stated in Community legislation or in notified national rules”).

In the UK the legal requirement (Health & Safety at Work Act) is that risk should be made as low as reasonably practicable (the ALARP principle – see next page).

In practice the CSM and ALARP principles are convergent, as use of a relevant industry code of practice or use of a system similar to one already in use in comparable applications may be accepted as meeting the ALARP principle by following industry best practice.

# ALARP

The ALARP principle:

Risk should be made As Low As Reasonably Practicable

A safety measure is not reasonably practicable if its cost is grossly disproportionate to the safety benefit which it would provide

Ways of demonstrating ALARP:

Cost/benefit analysis – show that the cost of preventing a fatality is greater than the nominal value of life. UK has financial values for preventing fatalities based on surveys of people's willingness to pay for safety.

Best practice – show that best practice in the industry has been applied. It is not considered reasonably practicable to do more than the best that others in the same industry achieve. Compliance with ENs may be enough to demonstrate ALARP.

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/26260d8a-8313-4d7f-8953-d0e2817fe234/79156527dba74db7fb38ff80349dc2be03d7bd0803acc4ce06bcbdee14913c7e.jpg)

# Engineering Safety Management

Safety Management can be defined as the organisational measures applied to ensure that an acceptable level of safety is maintained throughout the life of a system. It has much in common with Quality Management: both are concerned with the avoidance of loss.

What distinguishes Safety Management from Quality Management, or from the principles of good management in general, is that Safety Management must concern itself with events which are sufficiently improbable to be ignored by other aspects of management. For this reason hazard identification and risk assessment are prominent components of Safety Management.

The respective contributions of Quality Management and Safety Management to the safety of a system can be simply stated as follows: Quality Management ensures that the system does what was intended, while Safety Management ensures that what was intended was safe.

# Safety Management as a Process

The safety management process, especially in high-hazard industry sectors, such as nuclear power, aviation or petro-chemicals, is often depicted as 'Plan-Do-Check-Act' and can be likened to a closed-loop feedback control system, as illustrated in the figure on the right, which is based on the model used by the Health and Safety Executive in their guidance.

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/26260d8a-8313-4d7f-8953-d0e2817fe234/1e2b05e1c7936782d1f3ffbd60f6729fb278343b892f2dcd88ce87feb6e90562.jpg)

# Safety Management and Safety Integrity

The standards for safety-related electronic systems and software place particular emphasis on two aspects of engineering safety management: INDEPENDENCE and DOCUMENTATION.

# Independence of Roles

Many roles within an organisation, such as verifier, tester, validator or assessor, are concerned with confirming the safety of what has been produced by other roles, such as designers and installers. Independence between such roles may be required in order to reduce the probability of people in different roles suffering from the same misconceptions or making the same mistakes.

It is also important that people in roles which involve making judgements about the acceptability of a product or process from the point of view of safety should not be influenced by pressure from their peers or supervisors, or by considerations of commercial gain.

# Documentation

To engineer is essentially to generate or transform information, and engineering is a social activity involving collaboration and exchanges between individuals and organisations. Engineers work primarily with their brains, and documentation is the medium through which the product of this work is recorded and shared with others.

Ensuring the safety of complex systems is heavily dependent on large amounts of information being shared among all the parties concerned, including designers, operators, safety assessors, regulators and safety authorities. Documents form the principal medium of exchange of information, and there are established standards and guidelines for safety in systems engineering which set out requirements for what should be documented and by whom the documents should be reviewed and assessed

# Safety Case: Origins and Definitions

# safety case

the documented demonstration that the product complies with the specified safety requirements

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/26260d8a-8313-4d7f-8953-d0e2817fe234/4686ee39ebc8fdeae5405c92ff0c85045e8cc5b4bff8c81732d88348aebe4828.jpg)

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/26260d8a-8313-4d7f-8953-d0e2817fe234/ef774aee1ae93bce99d20d00a2f46bd89ac1562c457f0fe2417a0f3f1dfeee5a.jpg)

"A documented body of evidence that provides a convincing and valid argument that a system is adequately safe for a given application in a given environment"

In the term “Safety Case” the word “case” is used with the same meaning as in a law court – the evidence offered in court to support a claim.

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/26260d8a-8313-4d7f-8953-d0e2817fe234/bec4bed6f19ff7131670d3914817b6fd81ace9ef985532a45a81efcd13af86a0.jpg)

Safety cases were first used in the nuclear and off-shore oil industries to gain approval from their safety regulators

# Why Safety Cases?

- In a Safety Case regime the Developer has to demonstrate that the system is safe.  
- This is potentially more effective than relying on the Assessor or Approver investigating the system to find out if it is safe.  
- With complex systems only the Developer has sufficient knowledge of the system to produce the evidence of safety

# Structure and Content of a Safety Case

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/26260d8a-8313-4d7f-8953-d0e2817fe234/91eab3fb460093e7d0a89fa992cbde9314186a42482266370103a3d8338183ba.jpg)  
Railway applications - Communication, signalling and processing systems - Software for railway control and protection systems

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/26260d8a-8313-4d7f-8953-d0e2817fe234/88be506f3b765edca548a62a41ec23c31b27bba963bd9c7ce2b68cb33be33fe2.jpg)

# Types of Safety Case

Generic product Safety Case (independent of application)

A generic product can be re-used for different independent applications;

Generic application Safety Case (for a class of application)

A generic application can be re-used for a class/type of application with common functions;

Specific application Safety Case (for a specific application)

A specific application is used for only one particular installation.

The three types of safety case would apply to a programmable interlocking system as shown here. The signalling logic embodies the signalling principles of the railway network, while the geographical data configures each interlocking to its respective track and signal layout.

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/26260d8a-8313-4d7f-8953-d0e2817fe234/0ed61a76745d76dd8c9525e6726809e1e70d4ace986935bee60f59896fda896e.jpg)

# Part 2: Achieving Safety Integrity

# What is Safety Integrity?

Safety Integrity is defined as the likelihood of a system satisfactorily performing the required safety functions under all the stated conditions within a stated period of time.

The expression “required safety functions” includes the function of reverting to a safe state in the event of a failure.

To achieve acceptable safety integrity we need to know why failures occur and how components and systems behave in the event of failure.

Failures relevant to safety are commonly classified as being either random or systematic.

# Random and Systematic Failures

From the point of view of the user, all failures are random. If it was known when they would occur they could be prevented or avoided.

# Failure Categories

# Systematic failure

- Errors in requirements  
- Design and realisation inadequacies  
Manufacturing deficiencies  
- Inherent weaknesses  
- Software errors  
- Operating instruction deficiencies  
- Instruction inadequacies  
- Human errors  
- Etc.

# Random failure

- Operating modes  
- Environment  
- Stress degradation  
- Wear out  
-Over stress  
- Etc.

- The failure of physical components is determined by the laws of physics. They appear to happen at random because we do not know enough about the precise physical condition of the component.  
- The significant demarcation is between failures whose distribution is known and those whose distribution is unknown.  
- Failures for which there is reliable statistical data, i.e. failures of well-established components, are treated as Random Failures  
- Failures for which reliable statistics do not exist, e.g. design errors (especially software) or failures of new types of component, are treated as Systematic Failures.

# Designing to Take Account of Failure

In general, failures classified as "random" are those whose rate of occurrence cannot be made low enough to provide to provide sufficient assurance of safety. For such failures safety is assured by means of the fail-safe principle, which can be defined as "a design property of signalling equipment, and of the system within which it is used, that under failure conditions will provide safety for traffic".

In practice this is achieved by constructing signalling systems from subsystems or components having well-defined predictable failure modes and ensuring that failure states correspond to restrictive traffic conditions.

Fail-safety, can be achieved in three different ways:

$\succ$  Inherent fail-safety, where the system or subsystem is designed so that any credible failure mode of any of its component parts will result in a restrictive state.  
> Composite fail-safety. With this technique, each safety-related function is performed by at least two items. Each of these items shall be independent from all others, to avoid common-cause failures. Nonrestrictive activities can progress only if the necessary numbers of items agree.  
$\succ$  Reactive fail-safety. This technique allows a safety-related function to be performed by a single item, provided its safe operation is ensured by rapid detection and negation of any hazardous fault by another item.

# Inherent Fail-Safety: The Semaphore signal

Perhaps the simplest example of a fail-safe component is the semaphore signal with its counterbalance weight to restore the signal to the "on" position should the operating wire break.

Note that fail-safe behaviour also depends on the driver rod being sufficiently strong not to break or deform under any force which may be applied to it.

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/26260d8a-8313-4d7f-8953-d0e2817fe234/e2181a540c16bdf2522f0b5247d44ae9391fac155c71ee6c0225d9b14b12b39c.jpg)

# Inherent Fail-Safety: The Signalling Relay

The fail-safe characteristics of the signalling relay are at the heart of almost all classical electrical signalling safety. In British signal engineering practice the principal relay safety characteristics are an armature and contact operating mechanism with sufficient restoring forces from gravity and spring pressure to ensure that it will release when the coil is de-energised, and non-weldable contacts formed from mating and silver-impregnated carbon pairs.

Signalling circuitry using such relays is designed so that relays are required to be energised to enable a "proceed" signal aspect to be given. Any failure, such as a broken wire or high-resistance contact, will cause one or more relays in the circuit concerned to de-energise, in which case a restrictive signal aspect will be displayed.

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/26260d8a-8313-4d7f-8953-d0e2817fe234/ab3719dcac6d90669272dca0539f087a9d4060c9b198b08347de872d7c86ea90.jpg)

# Safety features of Signalling relay

Non-weldable contacts

Restoring spring

Non-magnetic stud to prevent armature being held by residual magnetism when relay de-energised

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/26260d8a-8313-4d7f-8953-d0e2817fe234/6a2732bc80629b39ba1946575eedeb494e448fdce36cfa8275e54d8f536b6eb5.jpg)

# Composite and Reactive Fail-Safety

Inherent fail-safety is difficult to achieve in electronic systems because they generally comprise a large number of electronic components with a wide variety of possible failure modes, so that it is not feasible to design so that no credible failure mode of any component will result in an unsafe state.

Inherent fail-safety has been achieved for relatively simple electronic devices, such as the transmitter and receiver units of audio frequency track circuits, but for more complex applications based on microprocessors and other large-scale integrated electronic components, for example signal interlockings, composite or reactive fail-safety, or often a blend of the two, is almost always the preferred solution.

Both techniques depend on there being a very low probability of simultaneous failures in independent parts of the overall system. This calls for the system design to ensure that the time to detect and react to individual failures is sufficiently short. It is also necessary to ensure that inherent fail-safety will be achieved with regard to common-cause failures which might result in multiple simultaneous failures.

# Composite Fail-Safety

Composite fail-safety not only requires two independent functional channels to agree in order to produce and output but also requires that neither channel will have detected a fault, typically by means of internal self-testing routines.

The ability to detect a first fault and isolate the faulty channel makes a significant contribution to safety. If the first fault were to remain undetected indefinitely, the probability of a similar fault occurring in the second channel during the life of the equipment would be far from negligible.

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/26260d8a-8313-4d7f-8953-d0e2817fe234/09264b6cab8d09b06bba3b414a7e67d41acaa2c31d6735161a473e545b1f1ec2.jpg)  
The probability of a 1st fault, combined with the probability of a 2nd fault occurring during the 1st fault detection-plus-negation time T, shall be less than the specified probabilistic target.

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/26260d8a-8313-4d7f-8953-d0e2817fe234/1302e5414cf89bfd4f1b3aa28f1b031ec525c1418256e2ca6675126181843bc9.jpg)

# Reactive Fail-Safety

In the event of a failure of Function A an unsafe output can be present until negated by the fault detection. Hence the value of T for reactive fail-safety is much shorter than the value for composite fail-safety.

Reactive fail-safety is to be found in relay interlocking, where failure of signal lamps, which are not inherently fail-safe, is protected by lamp-proving circuits which restrict the aspects of relevant signals when a lamp failure is detected.

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/26260d8a-8313-4d7f-8953-d0e2817fe234/c4a05fd505b1d82af3efc548650b226c5d17dca7987e4dfa525e1ae260d7ae18.jpg)  
Detection-plus-negation time T, after a fault in A, shall not exceed the specified limit for the duration of a transient, potentially - hazardous output.

# Common-Cause Failures

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/26260d8a-8313-4d7f-8953-d0e2817fe234/bdf875cb6a6847d2d1c089dcca03e0d87fc6f9f90e7d449e1d9dd1e81eb31718.jpg)

The Venn diagram and simple fault tree show how a common-cause failure (CCF) can undermine the protection given by composite fail-safety. A common-cause failure between function and fault detection would have a similar effect on reactive fail-safety.

# Example of Combination of Safety Techniques within a Signalling System

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/26260d8a-8313-4d7f-8953-d0e2817fe234/488cc7e8aea18ee4e8332d072500467cfaea23f25f49a6133c01c8fc51587e8e.jpg)

# Systematic Failures

"Need"

What the system is

intended to do

"Reality"

The environment in

which the system works

Errors of

intention

Overlooked

side effects,

special cases,

preconditions

Systematic failures result from errors which can occur at any point in the lifecycle of a system or an item of equipment.

Examples of such errors are shown on the right. It is not possible to use the fail-safe principle to protect against the effects of systematic failures because there is no way of ensuring that the only errors which can occur will be those which result in a restrictive state.

Protection against systematic failure depends on preventing or detecting and removing errors at each stage of the lifecycle. The development of safety-related software is a prime example of this approach.

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/26260d8a-8313-4d7f-8953-d0e2817fe234/379417f00e3ca370ed4f11a3c84820590d9e5be5e09c9d99f17edd6b4425d47a.jpg)

# The Advent of Software

The development of processor based systems in the 1980s brought the problem of software, which cannot be fully tested.

The focus of safety assurance then shifted from product to process.

# The Welding Analogy

You can't fully test software, so you rely on the production process and the competence of the software engineers

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/26260d8a-8313-4d7f-8953-d0e2817fe234/c913faa68ee14a41a1da2e535b4545678646b663730f16eadbb2cd7ee622806a.jpg)

You can't test every weld, so you rely on the welding process and the competence of the welder

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/26260d8a-8313-4d7f-8953-d0e2817fe234/3d0db6d37c6ab53d8bd5daf8389da1c55b3e90f3de00052d2cfb5343843572a3.jpg)

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/26260d8a-8313-4d7f-8953-d0e2817fe234/e4fc75abda415d80b6183b839af561dbe8e079d3f476a3da56fa961375a28f96.jpg)  
Solid State Interlocking

# The SIL Concept

- The concept of SIL (Safety Integrity Level) was introduced early in the development of standards for safety related software because there was no way of measuring the probability of unsafe failure of software.  
- There is still no way of measuring this probability.  
- Although it is not possible to determine a numerical value for the probability of failure, it is reasonable to believe that if more effective design and Verification & Validation methods are used, the probability will be lower.  
- If the best possible methods are used, the software will have the highest possible safety integrity. It was decided to have four categories of method, so that SIL 4 is the highest possible.  
- The SIL concept has been extended from software to cover all types of systematic failure, such as errors in requirements, design errors and manufacturing errors.

# The SIL Concept Illustrated

Safety integrity level

4  
3  
2  
1  
0

Description of safety integrity

Very High Integrity

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/26260d8a-8313-4d7f-8953-d0e2817fe234/a3921d8aa2d03da4c5826ab9c3b07cd9f6d25ba531f38c98394ea504f8c14232.jpg)

Basic Integrity

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/26260d8a-8313-4d7f-8953-d0e2817fe234/493653b6a4e45749bdae0e30c9b83102239a3e883c8fcb366147673c0b8746c1.jpg)

Increasing rigour and effectiveness of methods

# Definitions of SIL

- The following definitions are shared by standards BS EN 50126, 50128 and 50129

# safety integrity

ability of a safety-related system to achieve its required safety functions under all the stated conditions within a stated operational environment and within a stated duration

# safety integrity level

one of a number of defined discrete levels for specifying the safety integrity requirements of safety-related functions to be allocated to the safety-related systems

# software safety integrity level

classification number which determines the techniques and measures that have to be applied to software

# system safety integrity level

classification number which indicates the required degree of confidence that an integrated system comprising hardware and software will meet its specified safety requirements

# Principles of Development for SIL

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/26260d8a-8313-4d7f-8953-d0e2817fe234/db6da8de6d4cbe9775be824875fecea24c54f37f9ac602189dac7d5589b9bd18.jpg)

# BSI Standards Publication

Railway applications - Communication,

signalling and processing systems - Software

for railway control and protection systems

BS EN 50129:2018

Incorporating corrigendum April 2019

The principles applied in developing high integrity systems and software include, but are not restricted to:

top-down design methods  
> modularity  
> verified components and component libraries (mainly for software)  
> verification of each phase of the development lifecycle,  
$\succ$  clear documentation and traceability  
auditable documents  
> validation  
assessment  
> configuration management and change control  
> appropriate consideration of organisation and personnel competency issues

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/26260d8a-8313-4d7f-8953-d0e2817fe234/8b6c5a8fb7b2e484d65274ec4116479f9f2995268630fbe58057226aabd5254a.jpg)

Railway applications - Communication,

signalling and processing systems - Safety

related electronic systems for signalling

The standards EN 50129 (electronic systems) and EN 50128 (software) include tables of techniques and measures for implementing these principles to meet the required SIL

# Part 3: Safety of Data Transmission

# Railway

# Signalling and Data

# Transmission

The diagram shows a state-of-the-art signalling system where there are no lineside signals and vital data giving authority for train movements is transmitted to the train by radio. A fixed data link, which may use optical fibres or copper conductors for its transmission medium, transmits command and status data between lineside equipment and the control centre, and a speech link is also provided by radio between the signaller and the train driver. This system architecture is typical of that adopted for the European Train Control System (ETCS)

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/26260d8a-8313-4d7f-8953-d0e2817fe234/6fe63d10c9c9d8eadfd496ab4b2916f1c95056311f2919efcf515ae8e83bc882.jpg)

# Conceptual Model of Data Transmission System

Information may be transmitted through a hierarchy of electronic systems which may store, forward or otherwise manipulate the information. Hardware or software faults in any of these systems might corrupt the information in unpredictable ways. The vital information receiver and the safe process must be capable of distinguishing between valid and corrupt information. Ways of making this distinction include:

- All physical signals above a certain amplitude or within a certain frequency band  
- Digital data which satisfies particular coding rules  
- Messages which satisfy certain protocols, e.g. have correct addresses or valid time stamps

Based on the OSI model of open transmission systems  
![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/26260d8a-8313-4d7f-8953-d0e2817fe234/c245ae56bcbbfb861d0b9a3be81bbd93baec9dd9197392f0e0465c73647167ea.jpg)  
Failures, errors and noise may affect any component in the model

# Multidimensional View of Information

- Physical signal - within this dimension only the analogue value of the physical signal is considered.  
- Data - in this dimension information is generally considered as strings of binary digits, and the relevant information protection techniques focus attention on the patterns of digits, without any consideration of useful content or meaning.  
- Procedures - the information units considered are words consisting of groups of digits, but checks refer to protocol or syntax rather than meaning.  
- Content – in this dimension the meaning of transmitted information is taken into account in checking its correctness.

# Sources of Error

- Inherent characteristics, error generated by sources within the transmission system (e.g. thermal noise in resistors)  
- External influences (the electromagnetic environment), errors injected from sources outside the system, generally referred to as electromagnetic interference (EMI)  
- Equipment failure, errors which are solely the result of equipment failure within the system.

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/26260d8a-8313-4d7f-8953-d0e2817fe234/5279b2e3c8a03339727eb79ba5504c057f2fbc9eafd859f3e4b4ef4446ea4a22.jpg)

# Methods of Protecting Information Transmission

# Protection in the Physical Signal Dimension

$\triangleright$  Screening of cables and equipment housings  
The use of balanced twisted conductors in copper cables  
Suppression of interference at source  
$\triangleright$  Use of optical fibres as a transmission medium

# The Data Dimension – Coding

Repeat messages  
> Block coding  
$\triangleright$  Convolution or cyclic block coding

# Protection in the procedural dimension

$\succ$  Closed-loop protocols: receiver repeats message back to sender and awaits confirmation from sender before acting on message  
Time stamping: message contains time of origin – receiver will reject information which is too old  
$\succ$  Sender's address included in message - receiver will reject information from wrong sender, e.g. in the event of message routing errors or cross-talk

# Fail-Safe

The fail-safe principle is applied in the transmission of safety information by designing the receiving safe process to adopt a restrictive state in the event of errors being detected or loss of transmission