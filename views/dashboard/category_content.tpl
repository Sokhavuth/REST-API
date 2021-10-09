<!--views/dashboard/category_content-->
<link href='/static/styles/category_content.css' rel='stylesheet' />

<section class='Content'>
    <form action='/dashboard/category' method='post'>
        <a>ឈ្មោះ​ជំពូកៈ</a><input type='text' name="label" required />
        <a>តំណរភ្ជាប់ៈ</a><input type='text' name='link' required />
        <a>ពេល​បង្កើតៈ</a><input type='datetime-local' name='datetime' required />
        <a></a><input type='submit' value='បញ្ជូន' />
    </form>
</section>