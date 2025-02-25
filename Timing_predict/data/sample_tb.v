// Testbench for the sample module
`timescale 1ns/1ps
module sample_tb;
  reg clk;
  reg [3:0] a, b;
  wire [3:0] out;

  // Instantiate the design under test
  sample dut (.clk(clk), .a(a), .b(b), .out(out));

  // Clock generation
  initial begin
    clk = 0;
    forever #5 clk = ~clk;
  end

  // Stimulus and display
  initial begin
    a = 4'b0010;  // 2
    b = 4'b0001;  // 1
    #10;
    $display("Result: %d", out);  // Should print 3
    $finish;
  end
endmodule