<!--views/dashboard/index.tpl-->
% rebase('base.tpl')

<link href="/static/styles/partials/header.css" rel="stylesheet"></link>
<section class='Head'>
    <header class='region'>
        <div class='site-logo'>{{ data['siteLogo'] }}</div>

        <form action='/dashboard/search' method='post'>
            <select name="select">
                <option>ការផ្សាយ</option>
                <option>ជំពូក</option>
                <option>សៀវភៅ</option>
                <option>អ្នក​ប្រើប្រាស់</option>
            </select>
            <input type='text' name="q" placeholder="Search" required />
            <input type="submit" value='បញ្ជូន'​ />
        </form>

        <div class='logout'><a href='/dashboard/logout'>ចេញ​ក្រៅ</a></div>
    </header>
</section>

<link href="/static/styles/partials/body.css" rel="stylesheet"></link>
<section class='Body region'>
    %include('dashboard/menu.tpl')

    <%
    if 'index' in data['route']:
        include('dashboard/post.tpl')
    elif 'category' in data['route']:
        include('dashboard/category.tpl')
    end
    %>
</section>