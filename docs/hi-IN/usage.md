---
title: Usage and troubleshooting
description: एजेंट्स का चयन करें, टास्कबार आइकन को नियंत्रित करें और गायब एकीकरणों का निदान करें।
---

## एजेंट  खोलें

प्रेस करें **SUPER + A**, टास्कबार रोबोट पर क्लिक करें या किसी एजेंट के एप्लिकेशन एंट्री को चुनें। सेलेक्टर निष्पादन योग्य OpenCode/Codex इंस्टॉलेशन्स प्रदान करता है और जब mise मौजूद हो तब पहली बार उपयोग के लिए Claude Code इंस्टॉलेशन की पेशकश करता है। **Esc** बिना कुछ लॉन्च या डाउनलोड किए रद्द करता है।

टर्मिनल कॉलर की कार्य निर्देशिका को विरासत में प्राप्त करता है; ग्राफिकल लॉन्च आमतौर पर सत्र की होम निर्देशिका से शुरू होते हैं। जब आपको किसी विशेष कार्य निर्देशिका की आवश्यकता हो, तो परियोजना टर्मिनल से एक एजेंट शुरू करें।

## टास्कबार दृश्यता

Open **Control Center > Appearance > Taskbar > Icons > Optional modules**, toggle **AI Agents**, then **Apply**. The robot belongs to 

; if its drawer is collapsed, expand the utilities group. The preference is `group/right-2`, defaults to true, and survives regeneration. It controls only the icon: shortcuts and desktop entries remain available. Runtime availability can still hide an enabled icon.

## निदानात्मक कमांड

```sh
argvus-ai list
argvus-ai status
argvus-ai status --check
argvus-ai menu
argvus-ai launch opencode
argvus-ai launch codex
argvus-ai launch claude
```

 `/taskbar/icons/ai_agents_enabled` `list` केवल स्थापित एजेंटों की रिपोर्ट करता है। `status` वेबार JSON जारी करता है, जबकि `status --check` अपनी एग्ज़िट स्थिति के माध्यम से यह रिपोर्ट करता है कि कोई मेनू विकल्प स्थापित या स्थापित करने योग्य है या नहीं। केवल क्लॉड का चयन/लॉन्च करने से ही इसकी स्थापना शुरू हो सकती है; `run-claude` एक आंतरिक टर्मिनल प्रवेश बिंदु है।

यदि शॉर्टकट अभी भी पुराने संयोजन का उपयोग करता है, तो कंट्रोल सेंटर के कीबोर्ड शॉर्टकट पेज में इसके व्यक्तिगत ओवरराइड की जाँच करें; पैकेज्ड डिफॉल्ट इसे ओवरराइट नहीं करते। यदि रोबोट उपस्थिति सेटिंग्स लागू करने के बाद गायब हो जाता है, तो `argvus-appearance` को अपडेट करें और टास्कबार सेटिंग्स को पुनः उत्पन्न/लागू करें। सीधे उत्पन्न Waybar/Lua फ़ाइलों को संपादित करने से बचें।

यदि क्लॉड इंस्टॉलेशन विफल हो जाता है, तो टर्मिनल त्रुटियों, नेटवर्क एक्सेस और इंस्टॉल की गई माइज़ संस्करण की जांच करें, फिर क्लॉड को फिर से चुनें। होम से माइज़ क्वेरीज़ चलती हैं इसलिए प्रोजेक्ट-विशिष्ट कॉन्फ़िगरेशन किसी अलग टूल का चयन नहीं करता। रैपर को ग्राफिकल PATH में माइज़ शिम्स की आवश्यकता नहीं होती। OpenCode/Codex खोज ग्राफिकल PATH का उपयोग करती है, बिना शेल उपनाम या इंटरैक्टिव स्टार्टअप स्क्रिप्ट्स के।

Return to AI Agents.

Agents open in a centered floating Kitty window titled 

, with an ARGVUS header and footer. Press **Ctrl + E** to close the agent window. This shortcut is reserved by the frame; Esc and Ctrl+C remain available to the agent.

The dedicated Kitty profile 

 hides tabs and clears inherited shortcuts for tabs, splits and fullscreen. Clipboard shortcuts Ctrl+Shift+C and Ctrl+Shift+V remain available. Its generated configuration is `ARGVUS AI Agent` under the ARGVUS cache directory. The package Hyprland module floats and centers windows with class `ai-agents` argvus-ai  `kitty-tui/kitty-ai-agents.conf` `argvus-ai`   at 1399 × 920.

 for the installed and user paths. for the installed and user paths.(/docs/argvus-ai/).

वापस जाएँ[एआई एजेंट्स](/docs/argvus-ai/).
