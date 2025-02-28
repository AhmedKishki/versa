module blinky(
    input wire clk,           // System Clock
    output reg [7:0] leds     // LED Output (Active-Low)
);

    // Clock Divider Parameters
    parameter div_n = 25; // Adjust for desired blink speed

    // Clock Divider Registers
    reg [div_n-1:0] div_ctr = 0; // Counter for clock division
    reg slow_clk = 0;            // Divided clock signal

    // LED Sequence Index
    reg [2:0] index = 0; // 3-bit index for 8 LEDs

    // Clock Divider Logic
    always @(posedge clk) begin
        div_ctr <= div_ctr + 1'b1;
        if (div_ctr == 0) slow_clk <= ~slow_clk; // Toggle slow clock on overflow
    end

    // LED Blinking Logic (Sequential Shift)
    always @(posedge slow_clk) begin
        leds <= ~(8'b00000001 << index); // Active-Low: Invert bits
        index <= (index == 7) ? 0 : index + 1; // Reset at last LED
    end

endmodule
