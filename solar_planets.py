import cv2

img=cv2.imread("solar-system.jpg")



cv2.putText(img,
            "sun",
             (120,90),
             cv2.FONT_HERSHEY_COMPLEX,
             2,
             (255,255,255),  
             )
cv2.putText(img,
            "Mercury",
             (130,190),
             cv2.FONT_HERSHEY_COMPLEX,
             0.3,
             (255,255,255),  
             ) 
cv2.putText(img,
            " Venus",
             (200,260),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255),  
             )     
cv2.putText(img,
            "Earth",
             (290,260),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255),  
             )   
cv2.putText(img,
            "moon",
             (300,150),
             cv2.FONT_HERSHEY_COMPLEX,
             0.4,
             (255,255,255),  
             )    
cv2.putText(img,
            "Mars",
             (390,180),
             cv2.FONT_HERSHEY_COMPLEX,
             0.4,
             (255,255,255),  
             )  
cv2.putText(img,
            "Jupiter",
             (550,70),
             cv2.FONT_HERSHEY_COMPLEX,
             0.8,
             (255,255,255),  
             )                                                                   
cv2.putText(img,
            "Saturn",
             (750,130),
             cv2.FONT_HERSHEY_COMPLEX,
             0.8,
             (255,255,255),  
             )
cv2.putText(img,
            "Uranus",
             (960,140),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255),  
             )
cv2.putText(img,
            "Neptune",
             (1100,140),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255),  
             )                          
cv2.imshow("output",img)

cv2.waitKey(0)
cv2.imwrite("solar_planets.jpg",img)
