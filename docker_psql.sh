docker run \
    --name psql \
    --rm \
    -e POSTGRES_USER=${POSTGRES_USER} \
    -e POSTGRES_PASSWORD=${POSTGRES_PASSWORD} \
    -e POSTGRES_DB=${POSTGRES_DB} \
    -v ${POSTGRES_VOLUME}:/var/lib/postgresql/data
    -p 5432:5432 \
    -d postgres:9
