# WHC2021SIC Project Template

<!-- Replace Project Template by your team name in title and description -->

Project Template for the IEEE World Haptics Conference 2021 Student Innovation Challenge

https://2021.worldhaptics.org/sic/

## Authors

### Team

<!-- For each team member, duplicate this following subsection and update Name, biography, pronouns and website. Please store pictures under images/portraits/ and use only Name in CamelCase for filenames. -->

#### Name

<img alt="Name's picture" src="images/portraits/Name.jpg" width="100px" height="auto"/>

Name is ... <!-- insert biography -->
 
Find more information on their <!-- update pronouns--> [website](https://).

### Tactile Mirror

<!-- For each team member, duplicate this following subsection and update Name, biography, pronouns and website. Please store pictures under images/portraits/ and use only Name in CamelCase for filenames. -->

#### Diar Abdlkarim

<img alt="Diar's picture" src="images/portraits/diar.jpg" width="100px" height="auto"/>

Diar is a PhD student at the University of Bimirngham working on upper limb rehabilitation following nerve injury using virtual reality training. 
 
Find more information on his [website](https://diarkarim.com).

#### Davide Deflorio

<img alt="Davide's picture" src="images/portraits/davide.jpg" width="100px" height="auto"/>

Davide is a PhD student at the University of Bimirngham working on sensory mechanisms of tactile perception with psychophysics and computational modeling.
 

### Advisor

#### Massimiliano Di Luca

<img alt="Max's picture" src="images/portraits/Max.jpg" width="100px" height="auto"/>

Max is Senior Lecturer at the University of Birmingham in the Centre for Computational Neuroscience and Cognitive Robotics. He performs both fundamental and applied research to investigate how humans process multisensory stimuli, with an accent on understanding the temporal, dynamic, and interactive nature of perception. He uses psychophysical experiments and neuroimaging methods to capture how the brain employs multiple sources of sensory information and combines them with assumptions, predictions, and information obtained through active exploration.

Find more information on their [website](https://massimilianodiluca.info).


### Chairs

#### Christian Frisson

<img alt="Christian Frissons's picture" src="images/portraits/ChristianFrisson.jpg" width="100px" height="auto"/>

Christian Frisson is an associate researcher at the Input Devices and Music Interaction Laboratory (IDMIL) (2021), previously postdoctoral researcher at McGill University with the IDMIL (2019-2020), at the University of Calgary with the Interactions Lab (2017-2018) and at Inria in France with the Mjolnir team (2016-2017). He obtained his PhD at the University of Mons, numediart Institute, in Belgium (2015); his MSc in “Art, Science, Technology” from Institut National Polytechnique de Grenoble with the Association for the Creation and Research on Expression Tools (ACROE), in France (2006); his Masters in Electrical (Metrology) and Mechanical (Acoustics) Engineering from ENSIM in Le Mans, France (2005). 
Christian Frisson is a researcher in Human-Computer Interaction, with expertise in Information Visualization, Multimedia Information Retrieval, and Tangible/Haptic Interaction. Christian creates and evaluates user interfaces for manipulating multimedia data. Christian favors obtaining replicable, reusable and sustainable results through open-source software, open hardware and open datasets. 
With his co-authors, Christian obtained the IEEE VIS 2019 Infovis Best Paper award and was selected among 4 finalists for IEEE Haptics Symposium 2020 Most Promising WIP.

Find more information on his [website](https://frisson.re).

#### Jun Nishida

<img alt="Jun Nishida's picture" src="images/portraits/JunNishida.jpg" width="100px" height="auto"/>

Jun Nishida is **Currently** Postdoctoral Fellow at University of Chicago & Research Fellow at Japan Society for the Promotion of Science (JSPS PDRA) / **Previously** JSPS Research Fellow (DC1), Project Researcher at Japanese Ministry of Internal Affairs and Communications, SCOPE Innovation Program & PhD Fellow at Microsoft Research Asia / Graduated from Empowerment Informatics Program, University of Tsukuba, Japan. 

I’m a postdoctoral fellow at University of Chicago. I have received my PhD in Human Informatics at University of Tsukuba, Japan in 2019. I am interested in designing experiences in which all people can maximize and share their physical and cognitive capabilities to support each other. I explore the possibility of this interaction in the field of rehabilitation, education, and design. To this end, I design wearable cybernic interfaces which share one’s embodied and social perspectives among people by means of electrical muscle stimulation, exoskeletons, virtual/augmented reality systems. Received more than 40 awards including Microsoft Research Asia Fellowship Award, national grants, and three University Presidential Awards. Review service at ACM SIGCHI, SIGGRAPH, UIST, TEI, IEEE VR, HRI.

Find more information on their [website](https://junis.sakura.ne.jp/wp).

#### Heather Culbertson

<img alt="Heather Culbertson's picture" src="images/portraits/HeatherCulbertson.jpg" width="100px" height="auto"/>

Heather Culbertson is a Gabilan Assistant Professor of Computer Science at the University of Southern California. Her research focuses on the design and control of haptic devices and rendering systems, human-robot interaction, and virtual reality. Particularly she is interested in creating haptic interactions that are natural and realistically mimic the touch sensations experienced during interactions with the physical world. Previously, she was a research scientist in the Department of Mechanical Engineering at Stanford University where she worked in the Collaborative Haptics and Robotics in Medicine (CHARM) Lab. She received her PhD in the Department of Mechanical Engineering and Applied Mechanics (MEAM) at the University of Pennsylvania in 2015 working in the Haptics Group, part of the General Robotics, Automation, Sensing and Perception (GRASP) Laboratory. She completed a Masters in MEAM at the University of Pennsylvania in 2013, and earned a BS degree in mechanical engineering at the University of Nevada, Reno in 2010. She is currently serving as the Vice-Chair for Information Dissemination for the IEEE Technical Committee on Haptics. Her awards include a citation for meritorious service as a reviewer for the IEEE Transactions on Haptics, Best Paper at UIST 2017, and the Best Hands-On Demonstration Award at IEEE World Haptics 2013.

Find more information on her [website](https://sites.usc.edu/culbertson/).

## Contents

Generated with `npm run toc`, see [INSTALL.md](INSTALL.md).

Once this documentation becomes very comprehensive, the main file can be split in multiple files and reference these files.

<!-- Table of contents generated by running from repository root: npm run toc -->

<!-- toc -->

- [Abstract](#abstract)
- [Introduction](#introduction)
  * [Documentation](#documentation)
    + [Hardware](#hardware)
      - [Sensors wiring](#sensors-wiring)
    + [Software](#software)
- [Acknowledgements](#acknowledgements)
- [License](#license)

<!-- tocstop -->

## Abstract

<!-- Summarize your project: for now copy the short pitch from your proposal -->

## Introduction

<!-- Explain your project: for now copy the 300-word description from your proposal -->

### Documentation

#### Hardware

- Raspberry Pi 4 x 1
- Qwiic Hat for Raspberry Pi x 1
- MMA 8452Q Accelerometer x 1
- LRAs x 2
- TDA2030A Audio Amplifier module x 2 (other 18W audio amplifier module will work as well)
- 2 channels power supply (20W per channel)

<img alt="Wiring diagram" src="images/diagram.png" width="100px" height="auto"/>


##### Sensors wiring
1. Connect the piHat to Raspberry Pi
2. Connect the accelerometer to the piHat with Qwiic cable
3. Connect the audio amplifiers to power supply (5 or 12 V)
4. Connect the input of the audio amplifiers to the GPIO and GND pins on rpi 
—> the amp for the left LRA is connected to pin 12, the amp for the right LRA to pin 32
5. Connect the LRAs to the amplifiers output



Made with [drawio-desktop](https://github.com/jgraph/drawio-desktop/) (online version: [diagrams.net](https://www.diagrams.net/)).

<!-- see: https://www.diagrams.net/blog/embed-diagrams-github-markdown -->

#### Software

Libraries to install:  

smbus2
numpy
socket
struct


Running instructions:

(Softwares are written in Python 3)
1. Open file ‘mainRead.py’ in Thonny IDE (or any other IDE)
2. Run ‘mainRead.py’
3. Open LXTerminal
4. Go to the folder of ‘mainWrite.py’
5. Type ‘python3 mainWrite.py’ and press enter to run ‘mainWrite.py’

## Acknowledgements

<!-- Describe your software components -->

SIC chairs would like to thank Evan Pezent, Zane A. Zook and Marcia O'Malley from [MAHI Lab](http://mahilab.rice.edu) at Rice University for having distributed to them 2 [Syntacts](https://www.syntacts.org) kits for the [IROS 2020 Intro to Haptics for XR Tutorial](http://iros-haptics-tutorial.org/). 
SIC co-chair Christian Frisson would like to thank Edu Meneses and Johnty Wang from [IDMIL](http://idmil.org) at McGill University for their recommendations on Raspberry Pi hats for audio and sensors.

## License

This documentation is released under the terms of the Creative Commons Attribution Share Alike 4.0 International license (see [LICENSE.txt](LICENSE.txt)).
