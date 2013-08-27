.. include globals.rst
        
Welcome to Routines!
********************
        
Routines is a simple package that provides a single decorator for you to mark 
functions as tasks (routines) that should be executed on a regular schedule.
                
To use, simply do the following::
	
	from routines import Routine
	
	@Routine(60)
	def my_routine_task(b):
		print b
	
	my_routine_task('Hello!')
	my_routine_task('Yay!')
	
As a result of the above, "Hello!" and "Yay!" will print every 60 seconds.