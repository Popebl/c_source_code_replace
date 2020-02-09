


typedef struct{
    int data;
}t_data;

typedef struct{
    int index; //a container maybe have many element, use this to indicate unify ID
#ifndef IMPROVE
    int data;
#else
    t_data _data;
#endif
} t_struct;


t_struct global_struct;

original_demo_function()
{
  t_data *struct_variable = &global_struct;

  struct_variable->data = 0x88; //set value operation
  int local_data = struct_variable->data;//get value operation
}
