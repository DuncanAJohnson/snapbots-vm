def throw_interrupt_error():
    raise RuntimeError("Thread Interrupted")

globalName1 = 12.1
async def thread_id_0(vm_proxy):
    global globalName1
    move = vm_proxy.move
    await move(10)

