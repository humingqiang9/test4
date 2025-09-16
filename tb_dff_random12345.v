// Testbench for D Flip-Flop
`timescale 1ns / 1ps

module tb_dff;

    // Declare inputs and outputs
    reg clk;
    reg rst;
    reg d;
    wire q;
    wire qn;

    // Instantiate the DFF module
    dff uut (
        .clk(clk),
        .rst(rst),
        .d(d),
        .q(q),
        .qn(qn)
    );

    // Clock generation
    always #5 clk = ~clk;

    // Test procedure
    initial begin
        // Initialize inputs
        clk = 0;
        rst = 1;
        d = 0;

        // Reset the flip-flop
        #10 rst = 0;
        #10 rst = 1;

        // Apply test vectors
        #10 d = 0; // Hold 0
        #10 d = 1; // Set 1
        #10 d = 1; // Hold 1
        #10 d = 0; // Reset 0
        #10 d = 0; // Hold 0
        #10 d = 1; // Set 1
        #10 $stop; // Stop simulation
    end

endmodule