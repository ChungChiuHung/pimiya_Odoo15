python 版本 3.9

postgresql 版本 13

## Pull images from docker hub

### odoo

`docker pull pimiya/odoo`

### postgres

`docker pull pimiya/postgres`

## Start an Odoo instance

in directory /odoo/

`docker-compose up -d`

You can find the detail in docker-compose.yml file.

已移除使用 secret file, 可視情況補上。

## Setup

1. 進入 `docker` 安裝 `pypeg2` 與其他綠界電子發票相關套件

以 `root` 身分進入 Container

```sh
docker exec -it --user root {image id} /bin/bash
```

進入後安裝必要套件

```sh
apt-get update
pip install pypeg2
pip install ecpay_invoice3
apt-get install ttf-wqy-zenhei ttf-wqy-microhei -y
```

2. Odoo install `Dolimi Agriculture`

## docker compose config

```
services:
  web:
    image: odoo:15
    depends_on:
      - db
    ports:
      - "8069:8069"
    volumes:
      - odoo-web-data:/var/lib/odoo
      - ./config:/etc/odoo
      - ./addons:/mnt/extra-addons
  db:
    image: postgres:13
    environment:
      - POSTGRES_DB=postgres
      - POSTGRES_PASSWORD=odoo
      - POSTGRES_USER=odoo
      - PGDATA=/var/lib/postgresql/data/pgdata
    volumes:
      - odoo-db-data:/var/lib/postgresql/data/pgdata
volumes:
  odoo-web-data:
  odoo-db-data:
```

#### once you start the odoo instance, the addons and config folder will be created.

You can start to create custom addons and interactive with it.

## list of new tasks for 2nd stage

- [ ] 宅配通 API 出單串接
- [x] 綠界 invoice 電子發票(已完成測試中)
- [ ] 銷售流程簡化與收穀部分借貸與會計整合
