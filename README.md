<h1 align="center">Data Analytics Using Pandas</h1>

The repository was created to organize a work of Yana Santos, Lucas Andrade, Paulo Henrique and Augusto Anastácio to final
project of the third module of the Program Diversidade Tech, of Data Analytics, offered by Ada in a colaboration with Suzano.

##### The objetive is to load data from an API created by the teacher Thiago Medeiros of a fictional exporting company, then treat and analyze data using Pandas functions.

#### Flowchart of the work (adaped from Lucas Andrade's flowchart):

![Flowchart](https://user-images.githubusercontent.com/59098432/202789750-2c5ea7a4-bdba-4e36-9515-8cc32bdc0ee2.png)

<h1 align="center">Analysis by Yana Santos</h1>

The company's data were observed during a period of one year. The quantity of sold products on each month is presented as below.

<p align="center">
  <img width="700" height="300" src="https://user-images.githubusercontent.com/59098432/203857895-6d5e3138-eb89-4a8d-afd6-e4a6dff65304.png">
</p>

It's possible to observe that there is a significant irregularity between the quantities between the months. This difference must be investigated. Focusing on the month with the highest quantities of sold products (June) and the lowest one (May), the number of requests on each month may be analyzed. 

<p align="center">
  <img width="600" height="300" src="https://user-images.githubusercontent.com/59098432/203858398-2192e933-778a-459a-9b2c-f88cf999a019.png">
</p>

As indicated, the number of requests in June is three times larger than the number of requests in May. Futhermore, it must be analyzed if there is variation of the quantity of products between the requests. This observation must be done normalizing the quantity of products on each request by the number of requests.


