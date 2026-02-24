// Proof of concept: write a simple .xlsx file.
package main

import (
	"fmt"
	"log"

	"github.com/xuri/excelize/v2"
)

func main() {
	f := excelize.NewFile()
	sheet := "Sheet1"

	// Set some cells
	_ = f.SetCellValue(sheet, "A1", "Metric")
	_ = f.SetCellValue(sheet, "B1", "Value")
	_ = f.SetCellValue(sheet, "C1", "Period")
	_ = f.SetCellValue(sheet, "A2", "Revenue")
	_ = f.SetCellValue(sheet, "B2", 125.5)
	_ = f.SetCellValue(sheet, "C2", "TTM")
	_ = f.SetCellValue(sheet, "A3", "Margin %")
	_ = f.SetCellValue(sheet, "B3", 0.22)
	_ = f.SetCellValue(sheet, "C3", "MRQ")

	out := "output.xlsx"
	if err := f.SaveAs(out); err != nil {
		log.Fatal(err)
	}
	fmt.Printf("Wrote %s\n", out)
}
