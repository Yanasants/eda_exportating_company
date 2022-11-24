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

<p align="center">
  <img width="600" height="300" src="https://user-images.githubusercontent.com/59098432/203860894-7d28e51e-bd61-4a5e-98a1-d5aae249a6aa.png">
</p>

The graph shows a constancy on the quantity of products on the requests. Therefore, the difference of the quantities during the months ocurrs only because of the frequency of the requests. 

The company sells two types of products, the ones sold by kg and the other ones sold by unity. Comparing the quantity of products sold by type:

<p align="center">
  <img width="600" height="300" src="https://user-images.githubusercontent.com/59098432/203861565-84c10351-249d-4aff-abcb-4471e100ebb5.png">
</p>

As indicated, the quantity of products of kg type is more than 5 times larger than the quantity of unity type ones. But what about the sales amount per type?

<p align="center">
  <img width="600" height="300" src="https://user-images.githubusercontent.com/59098432/203862461-a9414203-f9fe-47af-8ed7-3399febb6545.png">
</p>

Otherwise, in terms of sales amount, the products of unity type have reached an amount bigger than the double of the amount of kg type products, although the quantity of the kg ones is significantly larger. Therefore, it's plausible to assert that the prices of unity type products are too much higher than the other ones. 

Checking the consolidated value (quantity x price) per type, the result is presented below.

<p align="center">
  <img width="600" height="300" src="https://user-images.githubusercontent.com/59098432/203863544-ca7744b0-a039-4fd3-b95f-54d5f52c3878.png">
</p>

This way, even though the prices of unity type products are highest, because of the high quantity of kg type products, the biggest part of the total sales amount of the company is due the kg ones. 






