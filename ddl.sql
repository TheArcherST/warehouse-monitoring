create table path
(
    id serial
        primary key
);

create table task_queue
(
    id serial
        primary key
);

create table warehouse
(
    id            serial
        primary key,
    city_name     varchar not null,
    task_queue_id integer not null
        references task_queue
);

create table task
(
    id      serial
        primary key,
    path_id integer not null
        references path
);

create table checkpoint
(
    id           serial
        primary key,
    warehouse_id integer not null
        references warehouse,
    local_id     integer not null,
    location_x   integer not null,
    location_y   integer not null
);

create table forklift
(
    id           serial
        primary key,
    warehouse_id integer not null
        references warehouse,
    local_id     integer not null
);

create table visit_record
(
    id            serial
        primary key,
    checkpoint_id integer   not null
        references checkpoint,
    forklift_id   integer   not null
        references forklift,
    created_at    timestamp not null
);


create table checkpoint_rel_path
(
    id            serial
        primary key,
    checkpoint_id integer not null
        references checkpoint,
    path_id       integer not null
        references path
);
