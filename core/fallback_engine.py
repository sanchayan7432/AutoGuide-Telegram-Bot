def fallback_answer(question, marks):

    q = question.lower()

    if "scheduler" in q:
        return (
            "1. The scheduler selects the next process from the ready queue. "
            "2. It ensures efficient CPU utilization and fair process execution. "
            "3. It manages CPU allocation using scheduling algorithms."
        )

    if "kernel" in q:
        return (
            "1. Monolithic kernel includes all services in one space, while microkernel keeps only core functions. "
            "2. Monolithic is faster; microkernel is more secure and modular. "
            "3. Microkernel uses message passing, increasing overhead."
        )

    return (
        "1. The concept is explained in a structured way. "
        "2. It ensures clarity and understanding. "
        "3. Key points are presented concisely."
    )