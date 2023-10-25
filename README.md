[NASA App Development Challenge](https://www.google.com/url?q=https://www.nasa.gov/learning-resources/app-development-challenge/about-nasa-app-development-challenge-adc/&sa=D&source=editors&ust=1698279144771368&usg=AOvVaw2C3_r5YBoE1gUMNQgzb9NS)

\- Team Name: Team Archers

\- Academic Year: 2023-2024

\- School: Arlington Tech

Introduction

This is our research document for the NASA’s App Development Challenge for high schoolers. Essentially, the task is to visualize lunar terrain data collected from the Artemis mission. After the data is visualized we have to make a path for the rover to travel to collect samples on different points of the designated location. We are permitted to use any technology that we choose. Additionally, we can choose which terrain data to visualize from five different locations. However, we are required to justify all of our choices. This research document contains all of our progress, information, and choices with justifications.

Helpful Links

[Mainpage](https://www.google.com/url?q=https://www.nasa.gov/learning-resources/app-development-challenge/about-nasa-app-development-challenge-adc/&sa=D&source=editors&ust=1698279144772719&usg=AOvVaw2fNKLAw3mgv6NAFhPLkIl6)

[Full Handbook](https://www.google.com/url?q=https://www.nasa.gov/wp-content/uploads/2023/08/adc-fy24-handbook-final-508.pdf&sa=D&source=editors&ust=1698279144772975&usg=AOvVaw2q-pANmNDcPno2tWhic6n2)

[Github Repository](https://www.google.com/url?q=https://github.com/1bMedina/NASA_ADC/tree/main&sa=D&source=editors&ust=1698279144773213&usg=AOvVaw2r2ndn17o_CdTt3PErRDB8)

[Region File Download](https://www.google.com/url?q=https://www.nasa.gov/learning-resources/app-development-challenge/adc-handbook-and-coding-components-2024/&sa=D&source=editors&ust=1698279144773477&usg=AOvVaw2kaTv4sQsVMUvcoJbUGwsL)

[Moon Trek](https://www.google.com/url?q=https://trek.nasa.gov/moon/&sa=D&source=editors&ust=1698279144773702&usg=AOvVaw1-lsrMPUE-v3x1tIMsK1pT)

Team Members:

  
[Olive Jeng](mailto:oj56563@email.vccs.edu)

[Blu Medina](mailto:bm83026@email.vccs.edu)

[Mayah Millhouse](mailto:mm90523@email.vccs.edu)

[Caleb O’Neal](mailto:co30649@email.vccs.edu)

[Sheel Shah](mailto:sss65273@email.vccs.edu)

[Jason Spitzak](mailto:js45463@email.vccs.edu)

[Kiersten Sproles](mailto:ks94855@email.vccs.edu)

Software
========

We decided to use python as our primary programming language. We decided on this language because python is the most simple and straightforward programming language to learn, has several libraries that we can utilize, and ensures everyone in our team can contribute because we all know python.

Libraries
=========

Since we decided to use python for this project. We had to come up with a list of modules in python that we could use for visualization and pathfinding. Below is a list of possible modules that we identified and could prove useful in this project. Each module contains a brief description about what the module is and a link to the documentation for more information.

The following libraries were considered for visualization:

*   [Plotly](https://www.google.com/url?q=https://plotly.com/python/3d-charts/&sa=D&source=editors&ust=1698279144776373&usg=AOvVaw06PrjuJ9iEVPh0nSaaCW4V)

*   [PyVista](https://www.google.com/url?q=https://pyvista.org&sa=D&source=editors&ust=1698279144776673&usg=AOvVaw2d5wmUnFLYaLZerMXYYxy6) 

*   [Ursina Game Engine](https://www.google.com/url?q=https://www.ursinaengine.org/&sa=D&source=editors&ust=1698279144776961&usg=AOvVaw0D4rfeQHxqYHbF69cD4rFe)

*   [Matplotlib](https://www.google.com/url?q=https://matplotlib.org/&sa=D&source=editors&ust=1698279144777253&usg=AOvVaw2ZtkupJaKfSYT0aShh2E4Z) 

*   [PyQtGraph](https://www.google.com/url?q=https://pyqtgraph.readthedocs.io/en/latest/getting_started/3dgraphics.html&sa=D&source=editors&ust=1698279144777614&usg=AOvVaw0hgdQrHh-gJmOJ7c8nakJS)

*   [VTK](https://www.google.com/url?q=https://pypi.org/project/vtk/&sa=D&source=editors&ust=1698279144777928&usg=AOvVaw3qAnC71y7qperoZJqjLPZA)

*   [Folium](https://www.google.com/url?q=https://python-visualization.github.io/folium/latest/&sa=D&source=editors&ust=1698279144778260&usg=AOvVaw0MYhA2Pg9cv8rthk8AE6G-)

The following libraries were considered for pathfinding:

*   [Pyrr](https://www.google.com/url?q=https://pyrr.readthedocs.io/en/latest/index.html&sa=D&source=editors&ust=1698279144778667&usg=AOvVaw3DD4BFoYUkQ4IWIG0Wvpqw)

*   [Navmesh](https://www.google.com/url?q=https://pypi.org/project/pynavmesh/1.0.0/&sa=D&source=editors&ust=1698279144778944&usg=AOvVaw07ftdqssk4GK8PNIEs8lk7)

We decided to use the Ursina Game Engine as our visualization library. We chose this specific library because we will have to visualize 10 million data points so we need a fast and powerful library that can handle that amount of data. Additionally, Ursina is very customizable, we can include a mini-map, as well as view the map from many different angles.

Landing Regions
===============

Below is a table for the five landing regions that we are required to choose from. For each location we have listed some pros and cons to help us come to the most logical conclusion.

Peak Near Shackleton

 - Relatively flat compared to other points
 - Permanently shadowed region within landing region

Connecting Ridge

*   Close to south pole
*   Less data collection

Nobile Rim 1

*   Rim of a crater

Faustini Rim A

*   Rim of a crater, steep terrain
*   More data collection points
*   Between 2 craters, good for data collection

Leibnitz Beta Plateau

*   Somewhat flat
*   Less data collection

Justification:  
  
In the end, we decided to choose Peak Near Shackleton. We decided on this because Peak Near Shackleton is relatively flat compared to the locations which makes traversing it much easier. In addition, it is closer to the south pole of the moon, than any other location. This is important because the samples collected in this location are more likely to contain traces of ice water which if found would be a groundbreaking discovery.

Things to do for the Video Presentation:

*   As part of the video presentation, teams must include a narrative on the challenges they encountered and how the challenges were solved.

*   The Storyboard Handout is for conceptualizing development of the app

Outreach:

[press release](https://www.google.com/url?q=https://nasagov.box.com/s/8m637cxzlr77960blf6845gcmcgp54r2&sa=D&source=editors&ust=1698279144783938&usg=AOvVaw3R8tbx2gOvHDqbb-lTohqz)

*   Arl now ([email](mailto:arlingtonnews@gmail.com))
*   Arlington magazine ([email](mailto:editorial@arlingtonmagazine.com))
*   NBC4 ([contact us page](https://www.google.com/url?q=https://www.nbcwashington.com/send-feedback/&sa=D&source=editors&ust=1698279144784788&usg=AOvVaw1RXWmVrwib0VxY9NT-dVuH))
*   WUSA9 ([contact page](https://www.google.com/url?q=https://form.typeform.com/to/HEVfdFSM?typeform-medium%3Dembed-snippet%26typeform-source%3Dwww.wusa9.com&sa=D&source=editors&ust=1698279144785082&usg=AOvVaw3BJ9jdOr1YgTYVSHpbEFTJ) )
*   Washington Post ([letters@washpost.com](mailto:letters@washpost.com) )
*   WJLA ([newsdesk@wjla.com](mailto:newsdesk@wjla.com) )
*   Fox 5 DC ([fox5dc@fox.com](mailto:fox5dc@fox.com) )
*   NBC Washington (contact link: ​​[https://www.nbcwashington.com/send-feedback/](https://www.google.com/url?q=https://www.nbcwashington.com/send-feedback/&sa=D&source=editors&ust=1698279144785898&usg=AOvVaw1DqHplUmes7y9ZrJaOJW7m))

*   Acc chronicle ([leahmcfarlane@apsva.us](mailto:leahmcfarlane@apsva.us))

Contact info:

Sheel Shah: [sss65273@email.vccs.edu](mailto:sss65273@email.vccs.edu)

Caleb O’Neal: [co30649@email.vccs.edu](mailto:co30649@email.vccs.edu)

Kiersten Sproles: [ks94855@email.vccs.edu](mailto:ks94855@email.vccs.edu)

Jason Spitzak: [js45463@email.vccs.edu](mailto:js45463@email.vccs.edu)

Olive Jeng: [oj56563@email.vccs.edu](mailto:oj56563@email.vccs.edu)

Mayah Millhouse: [mm90523@email.vccs.edu](mailto:mm90523@email.vccs.edu) 

Email to Dr Van Lare:

Dear Dr. Van Lare,

I am the leader of a NASA App Development Challenge team that we've created here at Arlington Tech. One of the main aspects of the project includes reaching out to the community, and informing social media platforms, news stations, and other students about our project and Artemis III. We need to have this sent out to news stations by mid November, as the whole project is due by early December. We would like to send our project to about 8 news stations. This includes: ARLnow, Arlington Magazine, NBC4, WUSA9, Washington Post, WJLA, Fox 5 DC, and NBC Washington. We also plan to publish an article with the ACC Chronicle. If you have any other news station suggestions, please let us know.

I’ve attached the press release format to this email.

Thank you,

Blu Medina

[https://nasagov.app.box.com/s/8m637cxzlr77960blf6845gcmcgp54r2](https://www.google.com/url?q=https://nasagov.app.box.com/s/8m637cxzlr77960blf6845gcmcgp54r2&sa=D&source=editors&ust=1698279144789883&usg=AOvVaw2unNwKFXpmqTgHUKBp_fTP)
