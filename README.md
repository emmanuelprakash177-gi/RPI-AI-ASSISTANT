![RGB RING](https://github.com/user-attachments/assets/a56a7376-3813-42c1-84a9-bb1a46e237d7)
# RPI AI ASSISTANT 
The voice assistant is going to be a Raspberry Pi 4B that will run and output audio through a speaker whenever I ask it a question. The Raspberry Pi will run ai model locally, and I plan on making it run offline, meaning it doesn't need to rely on the Internet.

* As i first version i want to create it in online using gemini api . 
I as a prototype.
* The next version i will create the assistant and full offline 


| Item | Description | Example/Link | Quantity | Unit Price (USD) | Total Price (USD) | Notes |
|------|-------------|--------------|----------|------------------|-------------------|-------|
| Raspberry Pi 4 | Model B, 4GB or 8GB RAM | [Raspberry Pi 4 Model B](https://www.amazon.in/Raspberry-Pi-Computer-Model-4GB/dp/B09TTNF8BT/ref=asc_df_B09TTNF8BT?mcid=18a8b491b4a931cbb7d1841c4d2f313d&tag=googleshopmob-21&linkCode=df0&hvadid=709936632702&hvpos=&hvnetw=g&hvrand=1605580361181321348&hvpone=&hvptwo=&hvqmt=&hvdev=m&hvdvcmdl=&hvlocint=&hvlocphy=9153181&hvtargid=pla-1679572971964&gad_source=1&th=1) | 1 | $83.00 | $83.00 | Main single-board computer; I  haven no a Raspberry Pi|
| MicroSD Card | 16GB or larger, Class 10/UHS-1 | [HP 32GB MicroSD Memory Card SDHC mi210 Class 10, UHS-I, U1 Card](https://www.amazon.in/HP-MicroSD-U1-TF-Card-32GB/dp/B07DJLFMPS/ref=asc_df_B07DJLFMPS?mcid=c24f05d0b83333eea533af24f2437081&tag=googleshopmob-21&linkCode=df0&hvadid=709935065239&hvpos=&hvnetw=g&hvrand=17142817298682784741&hvpone=&hvptwo=&hvqmt=&hvdev=m&hvdvcmdl=&hvlocint=&hvlocphy=9153181&hvtargid=pla-483238834551&gad_source=4&th=1) | 1 | (₹580)$6.50 | $6.50 | Holds OS and files |
| USB Microphone | Plug-and-play USB mic | [Array AM-C28 USB Plug & Play Conference](https://www.amazon.in/COOLCOLD-Cancelling-Microphone-Professional-Computer/dp/B08H2FJQ9Y/ref=sr_1_2_sspa?dib=eyJ2IjoiMSJ9.STp-CIzTEwwJTfywozlUgOuif7bI5-sgPyJhPONpvsXO0pLg8b9V6LMHrNlH7HswWVqsHnHtaYrtsp2T2RfUM9eiKi-GGJZAdchaUYJ7fNaTg-W728fcFzvmkb4OvhB5T_04uQcamUaYdhSma301W8tr_e-vtc_VQ8lL9vW0z6LwEquj_WnewqTmHOL4KnouGudYnXW3GntugCs6HasaMaJfdzMRtMc3fvcAVfpFNvpGNWfMcfOqFJqne-E-1AcWE9Bo_6u7EziJFGtLObGRUKwm6iLF3I6f862lT18oVtY.olzhURnUr-wdquuBwgxkv1pry7QNPdwb7QWNxe2ud30&dib_tag=se&keywords=USB+Microphone&qid=1767181509&sr=8-2-spons&aref=oMee4j1j0U&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1) | 1 | $6.00 | $6.00 | For voice input |
| Speaker | 3.5mm aux or Bluetooth | [Portronics 6W in Tune 6 HD Sound 2.0 Channel Portable Desktop PC Speaker, 3.5mm Audio Jack](https://www.amazon.in/Portronics-Channel-Portable-Desktop-Multimedia/dp/B0F1MSNCTY/ref=pd_sbs_d_sccl_2_18/524-2727408-4573007?pd_rd_w=APlJc&content-id=amzn1.sym.6d240404-f8ea-42f5-98fe-bf3c8ec77086&pf_rd_p=6d240404-f8ea-42f5-98fe-bf3c8ec77086&pf_rd_r=XXKPS2V30PB2Z13FN66W&pd_rd_wg=N4nnH&pd_rd_r=09f63b9d-6a3d-4ae3-b61a-c27049067e95&pd_rd_i=B0F1MSNCTY&psc=1) | 1 | $8.00 | $8.00 | Audio output . I have some old speaker|
| Carrying Case | Custom-designed enclosure | N/A (planned 3D print) | 1 | $10.00 | $10.00 | Designed for portability and protection |
| PCB | pcb and items  cost | pcb file | 1 | $10.00 |  $10.00  |  for rgb setup |
**Estimated Total Cost:** **$116**

<img width="1152" height="896" alt="1000052519" src="https://github.com/user-attachments/assets/6e16a859-324b-48eb-8652-a3978f025a13" />


Step-by-Step: 
1. To run this voice assistant, you have to be on your Raspberry Pi's terminal and check if your audio devices are connected to the device.
2. Download the necessary packages/libraries; 
4. The code interferes with the system, so the best practice is to run the code in a virtual environment

python3 -m venv .venv
source .venv/bin/activate


I want to create an ai assistant . Now a days am very much thinking about it . Then I got an idea to create a ai assistant fully offline. Running fully offline modelDiscription:

