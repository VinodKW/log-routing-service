# Log Routing System

## Docker Commands
### Running containers
#### Starting all containers in docker-compose file. 
```
docker-compose up --build
```
#### After successful run of containers, start the test container.
```
 TEST_ENABLED=true docker-compose up --build test
```


# Solution

## Observations

-   Most suitable design patterns is **Chain of responsibility**

    -   As we have only one server/observer running which could have multiple instances.

    -   The request contains events **(login/logout)** which can be handled using handlers in the pattern.

## 

## Service Tech Stacks

-   Language: Python3

-   Framework: Django4

-   API: Django RestFramework

-   Database: MySql

-   For asynchronous processing and buffering:

    -   Worker and Cron: Celery and Celery Beat

## 

## Solution Steps

-   Write the code for the mentioned pattern

-   See if data is getting stored in the db for each request or not.

-   Now change the direct db write architecture.

#### Json Objects Buffer

-   Introduce a shard file system.

-   Whenever object comes to API, accept it in async way and put it into one of the shard files in round robbin fashion.

#### Batch Insertion

-   Batch insertion of data every 30 seconds.

    -   Define a celery task which will beat every 30 seconds.

        -   The celery worker will flush each shard file in a round robbin fashion.

        -   The worker will then bulk insert all the gotten objects into the table.

### Edge Cases Resolution

-   Concurrency of data read and write operation into the local file system.

    -   This edge condition can be mitigated using the following techniques.

        -   Locking mechanism.

            -   Introduce a locking mechanism every time a process
                operates on a file and open the lock only when the
                operation gets completed.

        -   Sharding.

            -   This will remove the dependency on a single file and
                also help in scaling up the system as we can deploy n
                number of workers to operate on the file parallely
                after data gets insert into the files.



## Architecture
![log_routing_service_arch](https://github.com/VinodKW/log-routing-service/assets/40213599/3dcc0621-a520-4b6f-80b5-1c03ad135cd1)

