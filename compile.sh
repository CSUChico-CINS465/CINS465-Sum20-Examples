#!/bin/bash

echo "Compile WASM"
docker-compose run --workdir /code/hello-world rust_wasm wasm-pack build --target web
echo "Copy code to web static"
cp ./wasm/hello-world/pkg/hello_world.js ./mysite/myapp/js
cp ./wasm/hello-world/pkg/hello_world_bg.wasm ./mysite/myapp/js
echo "Collect Static files to cloud"
docker-compose run --workdir /code/mysite web python manage.py collectstatic --noinput