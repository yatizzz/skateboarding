% rebase('layout.tpl', title='Home Page', year=year)

<div class="jumbotron"
    style="background-image: url('/static/images/1.jpg'); color: #26211d"">
    <img src="static/images/4.jpg" width=300/>
    <p></p>
    <p class="lead" style="background-color: #382229; color: #e6e6e6">
    Skate is a free web framework for building great Web sites and Web applications using HTML, CSS and JavaScript.</p>
    <p><a href="" class="btn btn-primary btn-large" style="background-color: #7f2c35; border-color: #261417; color: #e6e6e6" >Learn more &raquo;</a></p>
</div>

<div class="row" style="background-color: #d37377">  
    <div class="col-md-4" style="background-color: #d37377; color: #26211d">
        <h2>About skating</h2>
        <p>
            Follow the link for the history of skateboarding
        </p>
        <p><a class="btn btn-default"  style="background-color: #7f2c35; border-color: #261417; color: #e6e6e6" href="/about">Learn more &raquo;</a></p>
    </div>
    <div class="col-md-4" style="background-color: #7f2c35; color: #e6e6e6">
        <h2>Russian skateboarding</h2>
        <p>Follow the link for the history of russian skateboarding</p>
        <p><a class="btn btn-default" style="background-color: #d37377; border-color: #261417; color: #26211d" href="/contact">Learn more &raquo;</a></p>
    </div>
    <div class="col-md-4" style="background-color: #d37377; color: #26211d">
        <h2>Feedback</h2>
        <p></p>
        <p><a class="btn btn-default" style="background-color: #7f2c35; border-color: #261417; color: #e6e6e6" href="">Send us an email &raquo;</a></p>
    </div>
    

</div>
<div>
    <h3 class="btn btn-default". > Ask a Question </h3>
        <form action="/home" method="post">
        <p><textarea rows="2" cols="50" name="QUEST" placeholder="Your question"></textarea></p> 
        <p><input type="text" size="50" name="ADRESS" placeholder="Your email"></p>
        <p><input type="submit" value="Send"></p>
       
</form>
 </div>