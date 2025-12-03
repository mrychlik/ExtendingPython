CFLAGS = -I/usr/include/python3.13
LDFLAGS = -L. -lmy.cpython-313-x86_64-linux-gnu

my.cpython-313-x86_64-linux-gnu.so:
	python build_api.py

main: main.o  
	gcc $(CFLAGS) main.o -o main

clean:
	rm *.o *.so
