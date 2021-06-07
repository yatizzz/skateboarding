% rebase('layout.tpl', title=title, year=year)
%import json

<head>
<title> Reviews </title>
<style>
    .content{
        width:500px;
        height:300px;
        border:1px;
        display:inline-block;
        color: #e6e6e6;
    }

p {
    font-family: Verdana, Arial, Helvetica, sans-serif; 
    font-size: 12pt; 
   }

    </style>
</head>
<body>

<div class="jumbotron" style="background-color: #7f2c35; border-color: #261417; color: #e6e6e6">
    <h1>Reviews</h1>

</div>
<h2 style="color: #e6e6e6"> Add your own review</h2>

<form action="/reviews" method='post' style="margin-bottom: 10px">
        <p><input rows="2" cols="55" name="TITLE" placeholder="Your review's title"></p>
        <p><textarea type="text" size="120" name="ADVANTAGES" placeholder="Advantages you noticed"></textarea></p>        
        <p><textarea type="text" size="120" name="LIMITATIONS" placeholder="Limitations you noticed"></textarea></p>
        <p><input rows="2" cols="55" name="AUTHOR" placeholder="Enter your name"></p>
        <p><input rows="2" cols="55" name="PHONE" placeholder="Enter your phone"></p>
        <p><input rows="2" cols="55" name="AUTHOR_EMAIL" placeholder="Enter your email"></p> 
        <p><input rows="2" cols="55" name="WRITTEN_DATE" placeholder="Date of writing of the review"></p> 
        <p><input type="submit" value="Add" class="btn-default"></p>

</form>

     <style>
     .btn-default{
        background-color: #7f2c35 ;
        color: #e6e6e6
     }

    .jumbotron{
        background-color: #7f2c35  
    }
    </style>

<br>
<br>
<h2 style="background-color: #7f2c35; border-color: #261417; color: #e6e6e6" > Reviews to read</h2>
%with open('./reviews.json') as reviews:
%data=json.load(reviews)
%for key, value in data.items():
    <div style="border-bottom: 3px solid #261417; color: #e6e6e6">
        <h3 style="margin-top:40px">
        {{value['title']}}
        </h3>
        <p>Advantages: 
        {{value['advantages']}}
        </p>
        <p>Limitations: 
        {{value['limitations']}}
        </p>
        <p style="font-size:10pt">
        By {{value['author']}}
        </p>
        <p style="font-size:10pt">
        Published on {{value['published_date']}}, written on {{value['written_date']}}
        </p>
        <p style="font-size:10pt">
        Phone {{value['phone']}}
        </p>
        <p style="font-size:10pt">
        Email {{value['author_email']}}
        </p>
    </div>
%end

</body>
