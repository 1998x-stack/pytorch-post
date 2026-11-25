# Autograd 第三批评审

第 07–09 篇：JVP、Hessian/HVP、Activation Checkpoint。当前 main 六篇及开放 PR 已查重。CPU 2.10.0+cpu 三个 demo 实际运行退出 0；预期 Git blob SHA：forward-mode-jvp 9619800f9ff514cbc7b3b933697074580f738ae3；higher-order-hessian 55661af07e1756d16a350659a7e4793d79b9b1bf；activation-checkpoint 70237005bd7d04491c7688f854db5f41b0bc69bc。使用 Baydin 综述与 Chen 2016 §4.3 正文；Pearlmutter 1994 仅题录核验，未读全文。注意 HVP 的实数 C² 假设、低层 dual level 限制、non-reentrant early stop 仅本例、RNG 设备边界及 O(n/k+k) 是理想化激活槽位而非总显存。无 GPU/速度/峰值内存实测。HTML CI 和部署以实际执行记录为准。
