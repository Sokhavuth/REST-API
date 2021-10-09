<!--views/dashboard/category-->
<link href='/static/styles/category.css' rel='stylesheet' />

<section class='Category'>
    <form action='/dashboard/category' method='post'>
        <a>ឈ្មោះ​ជំពូកៈ</a><input type='text' name="name" required />
        <a>តំណរភ្ជាប់​រូបៈ</a><input type='text' name='link' required />
        <a>ពេល​បង្កើតៈ</a><input type='datetime-local' name='datetime' required />
        <a></a><input type='submit' value='បញ្ជូន' />
    </form>
</section>