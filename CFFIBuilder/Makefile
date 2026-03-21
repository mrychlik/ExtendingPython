CFLAGS = -I/usr/include/python3.13
LDFLAGS = -L. -lmy.cpython-313-x86_64-linux-gnu

LIBRARY=my.cpython-313-x86_64-linux-gnu.so

all: $(LIBRARY) main

$(LIBRARY):
	python build_api.py

main: main.o  $(LIBRARY)
	$(CC) $(CFLAGS) main.o -o main $(LDFLAGS)

clean:
	rm *.o *.so
