hexchat.register("DEADBEEF", "1", "DeaDBeeF currently playing script")

local function get_np()
    local handle = assert(io.popen('deadbeef --noplaying "%a - %t 「%b」"'))
    local res = string.gsub(assert(handle:read("*a")), "\n", "")
    handle:close()
    hexchat.command("SAY np: " .. res)
    return hexchat.EAT_ALL
end

hexchat.hook_command("wp", get_np, '"/wp" to display currently playing DeaDBeeF track')
hexchat.print("hexchat.wp.deadbeef.lua loaded")
