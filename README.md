The Simpsons Tapped Out tool App
================================

The simpsons tapped out app client, UI the tool [source](https://github.com/schdub/tsto).

Install
------------
- [git ](https://git-scm.com)
- [vagrant](https://www.vagrantup.com)

Configuration
-------------

```bash
> git clone https://github.com/EdgarVaguencia/tstoApp.git
> cd tstoApp/vagrantSetup
> vagrant up
```

Fly
---

```bash
> vagrant ssh
> (tstoApp)vagrant@precise64:~$ /home/tstoApp/manage.py runserver 0.0.0.0:8000
```

Test
-----

Go [192.168.33.10:8000](http://192.168.33.10:8000)
