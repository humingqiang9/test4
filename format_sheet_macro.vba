Sub FormatSheet()
    Dim ws As Worksheet
    Set ws = ActiveSheet

    ' Format the header row
    With ws.Range("A1:D1")
        .Font.Bold = True
        .Font.Size = 12
        .Interior.Color = RGB(200, 200, 200)
        .Borders.LineStyle = xlContinuous
    End With

    ' Auto-fit columns
    ws.Columns("A:D").AutoFit

    ' Add a simple border around the data range
    ws.Range("A1:D10").Borders.LineStyle = xlContinuous

    MsgBox "Sheet formatted!"
End Sub