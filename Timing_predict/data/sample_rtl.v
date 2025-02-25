// RTL module definition
module sample (
  input wire clk,
  input wire [3:0] a, b,
  output reg [3:0] out
);
  always @(posedge clk) begin
    out <= a + b;  // Combinational logic example
  end
endmodule