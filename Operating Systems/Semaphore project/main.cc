/******************************************************************
 * The Main program with the two functions. A simple
 * example of creating and using a thread is provided.
 ******************************************************************/

#include <random>
#include <cstdlib>
#include <ctime>
#include "helper.h"

void *producer (void *id);
void *consumer (void *id);
void consume_start(int, int); 
void consume_end(int, int); 


int* queue; //circular queue with elements equal to the duration of each job
int buffersize; // size of circular queue
int num_job; //Number of Items produced per producer 
int in;  // buffer index number of the next produced job 
int out; // buffer index number of the next job to be consumed
pthread_mutex_t mutex1; // mutual exclusion lock to protect the critical section
int semid1 = sem_create(SEM_KEY1, 1); // semaphore id for jobs remaining in the queue
int semid2 = sem_create(SEM_KEY2, 1); // semaphore id for space remaining in the queue
  

int main (int argc, char **argv)
{
  //check whether the number of command line argument is correct
  if (argc != 5){
    fprintf(stderr, "error: 4 command line arguments needed");
    exit(EINVAL);
  }
  buffersize = atoi(argv[1]); // size of the queue
  num_job = atoi(argv[2]); //number of jobs to generate for each producer
  const int num_producer = atoi(argv[3]); //number of producers
  const int num_consumer = atoi(argv[4]);  //number of consumers
  in = 0;
  out = 0;

  queue = new int[buffersize]; // initialise the circular queue

  //initialise mutual exclusion lock
  pthread_mutex_init(&mutex1, NULL); 

  sem_init(semid1, 0, 0); // semaphore to check whether there is jobs left in the queue
  sem_init(semid2, 0, buffersize); //semaphore to check whether there is empty space in the queue
  
  //crease an array for producer thread and consumer thread
  pthread_t producerid[num_producer];
  pthread_t consumerid[num_consumer];


  // parameter to pass to the producer function to inform each thread its producer id  
  int prod_id[num_producer];  
  for (int i = 0; i < num_producer; i++){
    prod_id[i] = i+1;
  }

  // parameter to pass to the consumer function to inform each thread its consumer id 
  int cons_id[num_consumer];
  for (int i = 0; i < num_consumer; i++){
    cons_id[i] = i+1;
  }

  for (int i = 0; i < num_producer; i++){
    pthread_create(&producerid[i], NULL, producer, (void *) &prod_id[i]);
    //cout << "producer thread:" << i << "created" << endl;
  }

  for (int i = 0; i < num_consumer; i++){
    pthread_create(&consumerid[i], NULL, consumer, (void *) &cons_id[i]);
    //cout << "consumer thread:" << i << "created" << endl;
  }
  
  for (int i = 0; i < num_producer; i++){
    pthread_join(producerid[i], NULL);
  }
  
  for (int i = 0; i < num_consumer; i++){
    pthread_join(consumerid[i], NULL);
  }

  delete[] queue; // freeing the memory space ocupied by circular queue array

  pthread_mutex_destroy(&mutex1);
  sem_close(semid1);
  sem_close(semid2);

  return 0;
}

void *producer(void *id) 
{
  int producer_id = *(int *) id;
  for (int i = 0; i < num_job; i++){
    int result = sem_wait_timed(semid2, 0, 20);
    if (result == -1){
      break;
    }
    
    pthread_mutex_lock(&mutex1);
    
    random_device rd;
    int random_duration = (rd()%10) + 1;
    queue[in] = random_duration; // insert to the circular queue the duration of job created
    cout << "producer(" << producer_id << "): job id " << in; 
    cout << " duration " << queue[in] << endl;
    in = (in + 1)%buffersize;
    
    int rand_time = (rd()%5) + 1;
    pthread_mutex_unlock(&mutex1);
    sem_signal(semid1, 0);
    sleep(rand_time);
  }

  cout << "Producer(" <<  producer_id <<"): no more jobs to generate" << endl;
  pthread_exit(0);
  
}

//function to print output message when a consumer takes up a job
void consume_start(int consumer_id, int job_id){
  printf("consumer(%d): job id %d executing sleep duration %d\n",consumer_id, job_id, 
  queue[job_id]);
}

//function to print output message when a consumer finishes the job
void consume_end(int consumer_id, int job_id){
  printf("consumer(%d): job id %d completed\n", consumer_id, job_id);
}

void *consumer(void *id) 
{
  int consumer_id = *(int *) id;
  while(true){
    int result = sem_wait_timed(semid1, 0, 20);
    if (result == -1){
      break;
    }
    pthread_mutex_lock(&mutex1);
    int job_id = out;
    out = (out + 1)%buffersize;
    consume_start(consumer_id, job_id);
    pthread_mutex_unlock(&mutex1);
    //unsigned int sleep_time = queue[job_id];
    sleep(queue[job_id]);
    queue[job_id] = 0;
    sem_signal(semid2, 0);
    consume_end(consumer_id, job_id);
  }
  pthread_exit (0);
}
