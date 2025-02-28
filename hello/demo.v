module top(
    input clk,           // System clock input (drives sequential logic)
    output [7:0] led,    // 8-bit LED output (visual feedback)
    output [13:0] disp   // 14-segment display output (drives display segments)
);

    // Define a clock divider parameter
    // `localparam` is a constant that cannot be modified at runtime.
    // This controls how much the main clock is divided to create a slower clock signal.
    localparam div_n = 25;   

    // `reg` is used for storing values in **sequential logic** (flip-flops).
    reg clk_div;             // Holds the divided clock signal (flips between 0 and 1).
    reg [div_n-1:0] div_ctr; // 25-bit clock divider counter (stores clock cycles)

    // `always @(posedge clk)` → Runs this block **on every rising edge** of the clock.
    always @(posedge clk) begin
        div_ctr <= div_ctr + 1'b1;  // `<=` is a **non-blocking assignment**, meaning the update happens after the clock edge.
        clk_div <= (div_ctr == 0);  // When `div_ctr` overflows, `clk_div` toggles (acts as a slower clock).
    end

    // `\`include` imports another Verilog file (`pattern.vh`), containing predefined display patterns.
    `include "pattern.vh"

    // Pattern counter: Tracks which character pattern is currently displayed.
    // `$clog2(pat_len)` computes the number of bits needed to store `pat_len` values.
    reg [$clog2(pat_len):0] pat_ctr; 

    // `always @(posedge clk)` → A **sequential logic block** that executes on the rising edge of the clock.
    always @ (posedge clk) begin
        if (clk_div) begin  // Only update `pat_ctr` when `clk_div` pulses (slower clock).
            if (pat_ctr == 2*pat_len - 1) // If `pat_ctr` reaches the maximum value, reset it to 0.
                pat_ctr <= 0;
            else
                pat_ctr <= pat_ctr + 1'b1; // Otherwise, increment `pat_ctr` (scroll to next character).
        end
    end

    // `assign` creates **combinational logic** (does not use registers).
    // `{clk, ~pat_ctr}` concatenates the original `clk` signal with the inverted `pat_ctr` value.
    assign led = {clk, ~pat_ctr};  

    // `assign` creates **combinational logic** for display output.
    // `? :` is a **ternary operator** (a shortcut for `if-else`).
    // If `pat_ctr[0] == 1`, all segments turn ON (`14'h3FFF`).
    // Otherwise, it fetches the correct pattern from `display_pat[]` and inverts it (`~`).
    assign disp = pat_ctr[0] ? 14'h3FFF : ~(display_pat[pat_ctr[$clog2(pat_len):1]]);

endmodule
