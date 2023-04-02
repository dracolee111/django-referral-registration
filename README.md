<br>
<h1><b> <u>Accounts App </b></h1>
<h3>Author: <b><i>Draco</i></b> </h3>
<h3>Package: <i><b>Python, Django</b></i></b></h3>
<br>
<p><i>After searching the internet, and none satisfactory and simplified was found, I decided to create a suitable accounts package with customizable fields and referral logic.
<br>
<br>
It can be used as a starting point for all your account related projects.
<br>
<br>
<ul><b><u>Features are:</b></u></u>
<li> Account related transactions including sign-up, login, and referrals
<li> Custom User-Model with custom fields like main balance, referral balance, referrals, referred by, etc
<li> Referral model
<li> Deployable on <a href="https://render.com"><b>render</b></a> <g>using build.sh and and start.sh<g>
<li> Different database modules for <b>DEBUG=True</b> and <b>DEBUG=Fasle</b>

<li> Very Suitable for beginners
<li> Can also work as a PWA (Install as an app)
</ul>

<ul><u><b>Usage</b></u>
<br>
<li> If you use <u>Linux or MacOS</u> you can run <b>sh build.sh</b> & <b>sh start.sh</b>.
<br> * <b>build.sh</b> will automatically run collectstatic, migrate, and creatsu which will create a superuser with defined username and password.
<br> * <b>start.sh</b> will run the server using gunicorn and any other background process defined.  eg. <b>python manage.py background_process & gunicorn core.wsgi --log-file=-</b>
<li> If you use windows, you will have to run the commands one by one, then instead of gunicorn, you use py manage.py runserver.
<br>Alternatively, you can use GIT BASH to run the <b>build.sh</b> and <b>start.sh</b>
</i></p>
<br><br>
<center><u><b>Thanks</b></u></center>

<center>

       _________     __                ___           __________        __    __
      |   ___   |   |  |              /   \         |   _______|      |  |  /  /
      |  |___| /    |  |             /  ^  \        |   |             |  |_/  /
      |        >    |  |            / /___\ \       |   |             |   _  /
      |   ___  \    |  |           /  _____  \      |   |             |  | \  \
      |  |___|  |   |  |_______   /  /     \  \     |   |________     |  |  \  \
      |_________|   |__________| /__/       \__\    |____________|    |__|   \__\

</center>