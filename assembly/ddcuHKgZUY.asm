section .data
    hello db 'Hello', 0xA  ; String to print with newline character
    hello_len equ $ - hello ; Length of the string

section .text
    global _start

_start:
    ; Write system call
    mov eax, 4          ; sys_write system call number
    mov ebx, 1          ; file descriptor 1 is stdout
    mov ecx, hello      ; address of string to output
    mov edx, hello_len  ; number of bytes to output
    int 0x80            ; call kernel

    ; Exit system call
    mov eax, 1          ; sys_exit system call number
    mov ebx, 0          ; exit status
    int 0x80            ; call kernel