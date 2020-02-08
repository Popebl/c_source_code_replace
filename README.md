Purpose:
  I am doing a modularization work on a C project. It is hard to do a perfect design in the beginning. A resonable method is try many times to find the right one. This also means we will have a lot of coding work to do.
  Consider that valueble work is design not coding. So I want using tool to do some coding work. This tool is uesd to do code replacing work.
  If you konw any other tool like this, please let me konw.


principle:

    According C program language gramma.
    Use reguler experssion to find the right position and replace target.

Example:

    Demo project is following:

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

		  struct_variable->data = 0x88; //set value operation (memory accessing)
		  int local_data = struct_variable->data;//get value operation (memory accessing)

    Due to modularization, we should change memory accessing to via API.

	processed_demo_function()
	{
		t_data *struct_variable = &global_struct;

		struct_set_data_operation(struct_variable->index,0x88); //set value operation (API)
		int local_data = struct_get_data_operation(struct_variable->index); //get value operation (API)
	}



