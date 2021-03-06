SamacSys ECAD Model
235502/240866/2.46/2/3/Integrated Circuit

DESIGNSPARK_INTERMEDIATE_ASCII

(asciiHeader
	(fileUnits MM)
)
(library Library_1
	(padStyleDef "c165_h110"
		(holeDiam 1.1)
		(padShape (layerNumRef 1) (padShapeType Ellipse)  (shapeWidth 1.65) (shapeHeight 1.65))
		(padShape (layerNumRef 16) (padShapeType Ellipse)  (shapeWidth 1.65) (shapeHeight 1.65))
	)
	(textStyleDef "Default"
		(font
			(fontType Stroke)
			(fontFace "Helvetica")
			(fontHeight 50 mils)
			(strokeWidth 5 mils)
		)
	)
	(patternDef "PHEONIX-5_08PITCH-2PIN" (originalName "PHEONIX-5_08PITCH-2PIN")
		(multiLayer
			(pad (padNum 1) (padStyleRef c165_h110) (pt 0, 0) (rotation 90))
			(pad (padNum 2) (padStyleRef c165_h110) (pt 5.08, 0) (rotation 90))
		)
		(layerContents (layerNumRef 18)
			(attr "RefDes" "RefDes" (pt 0, 0) (textStyleRef "Default") (isVisible True))
		)
		(layerContents (layerNumRef 18)
			(line (pt -2.54 5.9) (pt 7.62 5.9) (width 0.1))
		)
		(layerContents (layerNumRef 18)
			(line (pt 7.62 5.9) (pt 7.62 -5.3) (width 0.1))
		)
		(layerContents (layerNumRef 18)
			(line (pt 7.62 -5.3) (pt -2.54 -5.3) (width 0.1))
		)
		(layerContents (layerNumRef 18)
			(line (pt -2.54 -5.3) (pt -2.54 5.9) (width 0.1))
		)
		(layerContents (layerNumRef 28)
			(line (pt -2.54 5.9) (pt 7.62 5.9) (width 0.1))
		)
		(layerContents (layerNumRef 28)
			(line (pt 7.62 5.9) (pt 7.62 -5.3) (width 0.1))
		)
		(layerContents (layerNumRef 28)
			(line (pt 7.62 -5.3) (pt -2.54 -5.3) (width 0.1))
		)
		(layerContents (layerNumRef 28)
			(line (pt -2.54 -5.3) (pt -2.54 5.9) (width 0.1))
		)
	)
	(symbolDef "1711725" (originalName "1711725")

		(pin (pinNum 1) (pt 0 mils 0 mils) (rotation 0) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 230 mils -25 mils) (rotation 0]) (justify "Left") (textStyleRef "Default"))
		))
		(pin (pinNum 2) (pt 0 mils -100 mils) (rotation 0) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 230 mils -125 mils) (rotation 0]) (justify "Left") (textStyleRef "Default"))
		))
		(line (pt 200 mils 100 mils) (pt 600 mils 100 mils) (width 6 mils))
		(line (pt 600 mils 100 mils) (pt 600 mils -200 mils) (width 6 mils))
		(line (pt 600 mils -200 mils) (pt 200 mils -200 mils) (width 6 mils))
		(line (pt 200 mils -200 mils) (pt 200 mils 100 mils) (width 6 mils))
		(attr "RefDes" "RefDes" (pt 650 mils 300 mils) (justify Left) (isVisible True) (textStyleRef "Default"))

	)
	(compDef "1711725" (originalName "1711725") (compHeader (numPins 2) (numParts 1) (refDesPrefix IC)
		)
		(compPin "1" (pinName "1") (partNum 1) (symPinNum 1) (gateEq 0) (pinEq 0) (pinType Bidirectional))
		(compPin "2" (pinName "2") (partNum 1) (symPinNum 2) (gateEq 0) (pinEq 0) (pinType Bidirectional))
		(attachedSymbol (partNum 1) (altType Normal) (symbolName "1711725"))
		(attachedPattern (patternNum 1) (patternName "PHEONIX-5_08PITCH-2PIN")
			(numPads 2)
			(padPinMap
				(padNum 1) (compPinRef "1")
				(padNum 2) (compPinRef "2")
			)
		)
		(attr "Manufacturer_Name" "Phoenix Contact")
		(attr "Manufacturer_Part_Number" "1711725")
		(attr "Mouser Part Number" "651-1711725")
		(attr "Mouser Price/Stock" "https://www.mouser.com/Search/Refine.aspx?Keyword=651-1711725")
		(attr "RS Part Number" "1895843")
		(attr "RS Price/Stock" "http://uk.rs-online.com/web/p/products/1895843")
		(attr "Allied_Number" "70054425")
		(attr "Allied Price/Stock" "http://www.alliedelec.com/phoenix-contact-1711725/70054425/")
		(attr "Description" "Non-Fused Terminal Block Through Hole, 2 Way, Solder, Nylon, 250 V")
		(attr "Datasheet Link" "http://docs-asia.electrocomponents.com/webdocs/1380/0900766b81380186.pdf")
	)

)
