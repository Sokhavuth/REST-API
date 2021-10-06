<!--views/index.tpl-->
% rebase('base.tpl')
<link href="/static/styles/index.css" rel="stylesheet"></link>

<section>
    <header>ទំព័រ​ចុះ​ឈ្មោះចូល​ទំព័រ​គ្រប់គ្រង</header>
    <form method="post" action="/login">
        <a>Email:</a><input type='email' required />
        <a>ពាក្យ​សំងាត់ៈ</a><input type='password' required />
        <a></a><input type='submit' value='បញ្ជូន' />
    </form>
</section>