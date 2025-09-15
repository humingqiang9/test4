program circle_area
    implicit none
    real :: radius, area, pi
    
    ! Define the value of pi
    pi = 3.141592653589793
    
    ! Prompt user for radius
    write(*,*) 'Enter the radius of the circle:'
    read(*,*) radius
    
    ! Calculate area using formula: area = pi * radius^2
    area = pi * radius * radius
    
    ! Display the result
    write(*,*) 'The area of the circle with radius ', radius, ' is:'
    write(*,*) area

end program circle_area