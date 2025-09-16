// Testbench for D Flip-Flop
`timescale 1ns / 1ps

module d_ff_testbench;

    // Inputs
    reg clk;
    reg rst_n;
    reg d;

    // Outputs
    wire q;
    wire q_n;

    // Instantiate the Unit Under Test (UUT)
    d_ff uut (
        .clk(clk),
        .rst_n(rst_n),
        .d(d),
        .q(q),
        .q_n(q_n)
    );

    // Clock generation
    always begin
        #5 clk = ~clk;
    end

    // Test procedure
    initial begin
        // Initialize Inputs
        clk = 0;
        rst_n = 0;
        d = 0;

        // Display header
        $display("Time\tclk\trst_n\td\tq\tq_n");
        $monitor("%0t\t%b\t%b\t%b\t%b\t%b", $time, clk, rst_n, d, q, q_n);

        // Release reset
        #15 rst_n = 1;

        // Apply test vectors
        #10 d = 1;
        #10 d = 0;
        #10 d = 1;
        #10 d = 0;

        // Finish simulation
        #20 $finish;
    end

endmodule